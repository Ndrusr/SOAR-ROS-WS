#!/usr/bin/env python

import rospy
from std_msgs import String

def talker():

    pubTalker = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        message = f"Hello World! {rospy.get_time()}"
        rospy.loginfo(message)
        pubTalker.publish(message)
        rate.sleep()
    
if __name__== "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass