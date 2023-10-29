#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose
from my_turtlebot_navigation.srv import NavMessage, NavMessageResponse
import time
import math

import rosparam
import actionlib
from send_coordinates_action_client import SendCoordinates

class GetCoordinates():
    
    def __init__(self):

        rospy.loginfo("starting get_coordinates service....")
        self.my_service = rospy.Service('/get_coordinates', NavMessage, self.service_callback) 

        self.rate = rospy.Rate(10)

        
    def service_callback(self, request):

        label = request.label
        response = NavMessageResponse()

        try:    
            corner = rosparam.get_param(label)
            response.message = "Parameters Sent to move_base"
        except Exception as e:
            rospy.loginfo(str(e))
        
        sendcordinates = SendCoordinates(label, corner)
        response.navigation_successfull = True
        
        return response
            
if __name__ == '__main__':
    rospy.init_node('get_coordinates_service_node', anonymous=True)
    getcoordinates_object = GetCoordinates()
    rospy.spin() 


