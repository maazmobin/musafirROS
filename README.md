# musafirROS
ROS node for musafir low level control


velocity.py
ROS Python NODE - subsribes to Twist Messages and Publishes String velocity Commands for MUSAFIR
Node Name: Velocity
Subscribe Topic name: /cmd_vel
Subscribe Topic name: Twist
Publisher Topic Name: msgForMotorControllerV3
Publisher Topic Type: String



motorController.py
ROS Python NODE - connects to Motor Controller via Serial Port, Subscribes/Publishes Serial String Data
Serial Port Name: /dev/nano at 115200
Node Name: motorControllerV3
Subscribe Topic name: msgForMotorControllerV3
Subscribe Topic name: String
Publisher Topic Name: PublishMotorController
Publisher Topic Type: String

Subscribed Messages are sent AS IS to Serial port
Only Publishes COMPLETE LINES form SERIAL PORT - when line ends with \n