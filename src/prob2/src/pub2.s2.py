#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16


def cb(res):
    res.data += 5 
    rospy.loginfo(f"Overall value after all these operations is: {res.data}")
    




def sub1():
    rospy.init_node("Hs" ,anonymous = True)
    rospy.Subscriber("Numm"  , Int16 , cb)
    rospy.spin()
    
    
    
    
 
 
sub1()
