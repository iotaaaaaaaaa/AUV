#!/usr/bin/env python3 

import rospy 
from std_msgs.msg import Int16


def Multiples_of_2():
    rospy.init_node("Mulof2"  , anonymous  = True)
    pubby = rospy.Publisher("Num"  , Int16  , queue_size = 10)
    rate = rospy.Rate(1)
    
    i = 2
    while not rospy.is_shutdown():
             rospy.loginfo(f"Multiples of 2: {i}")
             pubby.publish(i)
             i+=2
             rate.sleep()
             
             
             
 
Multiples_of_2()            
