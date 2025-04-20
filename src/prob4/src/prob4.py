#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def camera():
    rospy.init_node('camera_publisher', anonymous=True)
    pub = rospy.Publisher('cam', Image, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    bridge = CvBridge()

    # Simulate that there is no camera detected
    cap = cv2.VideoCapture(0)  

    if not cap.isOpened():
        rospy.loginfo("No camera detected.")  #error 
        return  

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret or frame is None:
            rospy.loginfo("Error: Camera not accessible or the frame is empty.")
            break

        msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        pub.publish(msg)

        # Display the camera feed using OpenCV
        cv2.imshow("Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('e'):  # Press 'e' to exit 
            break

        rate.sleep()

    cap.release()  
    cv2.destroyAllWindows()

camera()

