#!/usr/bin/env python

import serial


import rospy
from std_msgs.msg import String
ser = serial.Serial('/dev/ttyUSB0', 9600)

def talker():
    pub = rospy.Publisher('armAngles', String, queue_size=10)
    rospy.init_node('Arduino2PythonPub', anonymous=True)
    rate = rospy.Rate(1000) # 1000hz
    while not rospy.is_shutdown():
     	fullStr = ser.readline() #reads in the information on angles from arduino
        rospy.loginfo(str(fullStr))
        pub.publish(str(fullStr)) #publishes this information to topic 'armAngles'

#comes in as one big string, so turntable_shoulder_elbow_......
#use a0, a1, a2, a3, a4, a5 = fullStr.split("_") to split them into individual variables
#you also need to cleanup a5 with this line
#a5 = int(filter(str.isdigit, a5))
#which ensures its a number
#a0 = turntable
#a1 = shoulder
#a2 = elbow
#a3 = forearm rotation
#a4 = wrist up/down
#a5 = wrist rotation

        rate.sleep()

if __name__ == '__main__':
    try:

        talker()
    except rospy.ROSInterruptException:
        pass



#except KeyboardInterrupt:
   # fullStr = ""
   # print("END OF CODE")
        
    