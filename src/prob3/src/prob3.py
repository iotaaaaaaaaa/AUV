#!/usr/bin/env python3

import rospy
from prob3.msg import bot_pose  # custom msg bot_pose 


states = ['up', 'right', 'down', 'left']
cur_index = 1  # Start at 'right' assumption 

x = 0
y = 0

# Move the bot forward based on the current direction
def forward():
    global x, y
    state = states[cur_index]
    if state == 'up':
        y += 1
    elif state == 'down':
        y -= 1
    elif state == 'left':
        x -= 1
    elif state == 'right':
        x += 1

def turn_left():
    global cur_index
    cur_index = (cur_index - 1) % 4

# Turn the bot right (update the state)
def turn_right():
    global cur_index
    cur_index = (cur_index + 1) % 4 # circular looping between the states


def tracker():
    pub = rospy.Publisher('bot_position', bot_pose, queue_size=10)
    rospy.init_node('bot_publisher', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        command = input("Enter the direction in which bot should move:(forward / turn left / turn right): ")

        if command == "forward":
            forward()
        elif command == "turn left":
            turn_left()
        elif command == "turn right":
            turn_right()

        msg = bot_pose()
        msg.x = x
        msg.y = y
        msg.direction = states[cur_index]  # Setting the direction based on current state
        
        pub.publish(msg)
        rate.sleep()

tracker()

