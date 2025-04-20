#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def cammy():
    rospy.init_node('camera_publisher')
    pub = rospy.Publisher('edg', Image, queue_size=10)
    cap = cv2.VideoCapture(0)
    bridge = CvBridge()
    
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            continue

        # Edge detection
        edges = cv2.Canny(frame, 100, 200)
        
        # Convert to ROS Image and publish
        img_msg = bridge.cv2_to_imgmsg(edges, encoding='mono8')
        pub.publish(img_msg)
        rate.sleep()

    cap.release()


cammy()
