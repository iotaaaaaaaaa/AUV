#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()
def callback(data):
  
    # Converting  the ROS Image message to OpenCV format
    cv_image = bridge.imgmsg_to_cv2(data, "mono8")
    
    # Displaying  the image
    cv2.imshow("Edge Detection", cv_image)
    cv2.waitKey(1)

def view():
    rospy.init_node('camera_subscriber')
    
    rospy.Subscriber('edg', Image, callback)  # sub  with the topic edg
    rospy.spin()

    cv2.destroyAllWindows()


view()
