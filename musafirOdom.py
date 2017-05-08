import math
from math import sin, cos, pi

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from std_msgs.msg import String

x = 0.0
y = 0.0
th = 0.0

vx = 0.1
vy = -0.1

def callback(data):
	message=data.data
	if message.count(',')==7 and message.startswith('e'):
		odomDataList = message.split(",")
		x=float(odomDataList[3])
		y=float(odomDataList[4])
		th=float(odomDataList[5])
        # is there a way to publish correct Velocities as well ?
        # along with ECHO of Pose, we could get Velocity echo as well
        # Depends if we REALLY REALLY need it.
		vx=float(odomDataList[6])
		vy=float(odomDataList[7])
        # what is at place 6 and 7 ??
		vth=0
#		print("-->>"+str(x)+","+str(y)+","+str(th)+","+str(vx)+","+str(vy))
		odom_broadcaster = tf.TransformBroadcaster()
        	odom_broadcaster.sendTransform((x, y, 0.),
                	tf.transformations.quaternion_from_euler(0, 0, th),
                	rospy.Time.now(),
                	"base_link",
                	"odom")
        	# translation, rotation, time, child frame, parent frame
        	current_time = rospy.Time.now()
        	odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
        	odom.header.stamp = current_time
        	odom.header.frame_id = "odom"
        	odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))
        	odom.child_frame_id = "base_link"
        	odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))
        	odom_pub.publish(odom)
        print(message)
        # is it necessary to print this - we can always rostopic echo the topics

if __name__ == '__main__':
    # why no try and spin ???
    # see if there is any official ROS Python Node code for Subscriber and Publisher
	rospy.init_node('odometry_publisher')
    odom = Odometry()
    odom_broadcaster = tf.TransformBroadcaster()
	odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
	sub = rospy.Subscriber("PublishMotorController", String, callback)
	rospy.spin()
    