#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64

pub = rospy.Publisher('output', Int64, queue_size=10)

def callbackFn2(msg):
    pub.publish(msg.data**2)

def operator():
    rospy.init_node('operator', anonymous=True)
    sub = rospy.Subscriber('input', Int64, callbackFn2)
    rospy.spin()

if __name__ == '__main__':
    operator()