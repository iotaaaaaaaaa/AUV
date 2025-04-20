#!/usr/bin/env python3

import rospy
from prob3.msg import bot_pose  # Custom msg bot_pose

def callback(msg):
    rospy.loginfo("Bot's Current Position: x = %d, y = %d, Direction = %s", msg.x, msg.y, msg.direction)

def tracker_subscriber():
    rospy.init_node('bot_subscriber', anonymous=True)

    rospy.Subscriber('bot_position', bot_pose, callback)

    rospy.spin()
    
    
    
tracker_subscriber()
