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
    # a5 = int(filter(str.isdigit, a5))
    # rospy.loginfo("a5 is " + str(a5))

    #0 ~ 1023 Pin value range

    # After starting, the output of pins from the initial (physical position) to the highest (physical position) is converted to PWM -> Servo
    # A0 turntable 0-1023
    # A1 SHOULDER 250-476
    # A2 ELBOW    440-0(-140?)
    # A3 FOREARM  22-616 
    # A4 WRISTUD  517-64
    # A5 WRISTROT 0-1023
    a0 = int(filter(str.isdigit, a0))
    a0 = 750 - a0

    a1 = int(filter(str.isdigit, a1))
    a1 = 476 - (a1 - 250)
    
    a2 = int(filter(str.isdigit, a2))
    a2 = - (a2 - 440)
    if a2 < 0:
            a2 = 0
    #-140? 

    a3 = int(filter(str.isdigit, a3))
    a3 = 616 - (a3 - 22)

    a4 = int(filter(str.isdigit, a4))
    a4 = 64 - (a4 - 517)
  
    a5 = int(filter(str.isdigit, a5))
    a5 = 1023 - a5

    #MAX-Offset to achieve Implement mirror motion
    pwm.set_pwm(0, 0, int(a0))
    pwm.set_pwm(1, 1, int(a1))
    pwm.set_pwm(2, 2, int(a2))
    pwm.set_pwm(3, 3, int(a3))
    pwm.set_pwm(4, 4, int(a4))
    pwm.set_pwm(5, 5, int(a5))

   
    # pwm.set_pwm(5, 5, int(a5))
    # pwm.set_pwm(4, 4, int(a4))
    
def listener():

    rospy.init_node('ReversePuppetArmSub', anonymous=True)

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
