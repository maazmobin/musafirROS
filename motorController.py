import sys,serial
import threading
import __future__
from serial.tools import list_ports
import math
import time
import tf
import rospy
from std_msgs.msg import String

if sys.version_info.major < 3:
	import thread as _thread
else:
	import _thread

serialString =""
ErrorSerial = True

def read_from_port(ser):
	global serialString , ErrorSerial
	while True:
		reading = ser.readline().decode()
		if reading!= "":
			if ErrorSerial == True:
				serialString += reading
			else:
				serialString = reading
			if "\n" not in reading:
				ErrorSerial = True
			else:
				ErrorSerial = False
				# print (serialString)
				pubRobotV3.publish(serialString)
		reading = ""

def write_to_port(data):
        message=str(data.data)
        serial_port.write(message)

if __name__ == '__main__':
	try:
		print("\n Note:")
		print("Publishing Serial String of Motor Controller: 'PublishMotorController'")
		print("Subscribe Serail String for Motor Controller: 'msgForMotorControllerV3'")
		pubRobotV3 = rospy.Publisher('PublishMotorController', String, queue_size=1)
	        rospy.Subscriber("msgForMotorControllerV3", String, write_to_port)
		rospy.init_node('motorControllerV3')

		serial_port = serial.Serial('/dev/nano', 115200,timeout=0)
		serThread = threading.Thread(target=read_from_port, args=(serial_port,))
		serThread.setDaemon(True)
		serThread.start()

		rospy.spin()

	except serial.SerialException:
		print "Serial Port Error..."

	except KeyboardInterrupt:
	        print "Key-interrupt"
        	sys.exit(0)

	sys.exit(0)
