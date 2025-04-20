#!/usr/bin/env python3 

import rospy
from std_msgs.msg import Int16 

def callback(i):
     res = i.data * 10
     pub.publish(res)



def sub():
    global pub
    rospy.init_node("Multiples_of_10"   , anonymous = True)
    pub = rospy.Publisher("Numm"  , Int16  , queue_size = 10)
    rospy.Subscriber("Num"  , Int16 , callback)
    rospy.spin()
    
    
    

sub()  
