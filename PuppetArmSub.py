#!/usr/bin/env python
import rospy
import Adafruit_PCA9685
from std_msgs.msg import String

pwm = Adafruit_PCA9685.PCA9685();
pwm.set_pwm_freq(60) 

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)
    fullStr = str(data)
    a0, a1, a2, a3, a4, a5 = fullStr.split("_")
    a5 = int(filter(str.isdigit, a5))
    a0 = int(filter(str.isdigit, a0))
    rospy.loginfo("a3 is " + str(a3))
    rospy.loginfo("a5 is " + str(a5))
    pwm.set_pwm(0, 0, int(a0))
    pwm.set_pwm(1, 1, int(a1))
    pwm.set_pwm(2, 2, int(a2))
    pwm.set_pwm(3, 3, 320)#320
    pwm.set_pwm(5, 5, 285)#285
    pwm.set_pwm(4, 4, int(a4)) # 517 to lock at parallel
    
def listener():

    rospy.init_node('PuppetArmSub', anonymous=True)

    rospy.Subscriber("armAngles", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


        #pwm.set_pwm(0, 0, int(a0))
        #pwm.set_pwm(1, 1, int(a1))
        #pwm.set_pwm(2, 2, int(a2))
        #pwm.set_pwm(3, 3, int(a3))
        #pwm.set_pwm(4, 4, int(a4))
        #pwm.set_pwm(5, 5, int(a5))
