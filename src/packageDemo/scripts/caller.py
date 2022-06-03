#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def callbackFn(msg):
    rospy.loginfo(f'Recieved: {msg.data}')

def caller():
    pub = rospy.Publisher('input', Int64, queue_size=10)
    rospy.init_node("caller", anonymous=True)
    sub = rospy.Subscriber('output', Int64, callbackFn)
    count = 0
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        count += 1
        pub.publish(count)
        rate.sleep()

if __name__== "__main__":
    try:
        caller()
    except rospy.ROSInterruptException:
        pass