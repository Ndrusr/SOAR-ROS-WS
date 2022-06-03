#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callbackFn(msg):
    rospy.loginfo("Recieved: " + msg.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    subListener = rospy.Subscriber('chatter', String, callbackFn)
    rospy.spin()

if __name__ == '__main__':
    listener()