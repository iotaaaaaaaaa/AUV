#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


name  = input("Enter your name (Jolyne/Joestar): ")  #taking input from the user 

def callback(msg):
    sender_name = msg.data.split(":")[0]     
    if sender_name != name:                       #if i enter same name in two terminals i need to not show anything so for that checking that the user who sent the msg is same  or not 
        rospy.loginfo(msg.data)

rospy.init_node("Convo", anonymous=True)          #creating a node 
pubby = rospy.Publisher("Chat", String, queue_size=10)           #also publisher and sending to the topic Chat
rospy.Subscriber("Chat", String, callback)
rate = rospy.Rate(1)  

print(f"Yeah now u can send u r message @{user_name}.")  


while not rospy.is_shutdown():
    msg = input(f"{user_name}: ")
    pubby.publish(f"{user_name}: {msg}")
    rate.sleep()

