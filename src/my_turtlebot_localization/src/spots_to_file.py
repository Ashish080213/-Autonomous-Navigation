#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from my_turtlebot_localization.srv import MyServiceMessage, MyServiceMessageResponse
import time
import math
import yaml

class SaveSpot():
    
    def __init__(self):

        self.spots = {}
        self.points = {}

        self.my_service = rospy.Service('/save_spot', MyServiceMessage, self.service_callback) 
        self.amcl_pose_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.sub_callback)       

        while self.amcl_pose_sub.get_num_connections()<1:
            rospy.loginfo("Waiting for the /amcl_pose topic")
            time.sleep(0.1)
        rospy.loginfo("---------------------------------------------------------------")
        rospy.loginfo("Getting data from the /amcl_pose topic")

        self.sub_msg_pose = PoseWithCovarianceStamped()

        self.rate = rospy.Rate(10)
    
    def addspots(self, label, pose):
        pos = pose.position
        orient = pose.orientation
        self.spots[label] = {'position':{'x':pos.x, 'y':pos.y, 'z':pos.z},
        'orientation':{'x':orient.x, 'y':orient.y, 'z':orient.z, 'w':orient.w}}
 
    def sub_callback(self, msg):
        
        self.sub_msg_pose = msg
        self.pose = self.sub_msg_pose.pose.pose

    def service_callback(self, request):

        label = request.label
        response = MyServiceMessageResponse()
        # rospy.loginfo(self.sub_msg_pose)

        if label != "end":


            self.points[label] = self.pose
            self.addspots(label, self.pose)
            
            # rospy.loginfo(self.points[label])
            response.message = label + " Saved"
            rospy.loginfo(label + " Position Saved Successfully")
        
        else:

            with open("/home/user/catkin_ws/src/my_turtlebot_localization/text/spots.yaml","w") as outfile:
                yaml.dump(self.spots, outfile, default_flow_style=False)

            f = open("/home/user/catkin_ws/src/my_turtlebot_localization/text/spots.txt","w")
    
            for key in self.points:

                f.write(str(key) + "\n--------------------------\n" + str(self.points[key]) + "\n--------------------------\n")

            f.close()


            response.message = "File Saved Successfully!!!"
            response.navigation_successfull = True
        
        return response
            
if __name__ == '__main__':
    rospy.init_node('spot_recorder', anonymous=True)
    spot_object = SaveSpot()
    rospy.spin() 



# import rospy
# from geometry_msgs.msg import PoseWithCovarianceStamped, Pose
# from my_turtlebot_localization.srv import MyServiceMessage, MyServiceMessageResponse
# import time
# import math

# class SaveSpot():
    
#     def __init__(self):

#         self.points = {}

#         self.my_service = rospy.Service('/save_spot', MyServiceMessage, self.service_callback) 
#         self.amcl_pose_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.sub_callback)       

#         while self.amcl_pose_sub.get_num_connections()<1:
#             rospy.loginfo("Waiting for the /amcl_pose topic")
#             time.sleep(0.1)
#         rospy.loginfo("---------------------------------------------------------------")
#         rospy.loginfo("Getting data from the /amcl_pose topic")

#         self.sub_msg_pose = PoseWithCovarianceStamped()
#         self.robot_pose = Pose()

#         self.rate = rospy.Rate(10)

 
#     def sub_callback(self, msg):
        
#         self.sub_msg_pose = msg
#         self.robot_pose = msg.pose.pose
        
#     def service_callback(self, request):

#         label = request.label
#         response = MyServiceMessageResponse()
#         # rospy.loginfo(self.sub_msg_pose)

#         if label != "end":

#             # self.points[label] = self.sub_msg_pose
#             self.points[label] = self.robot_pose
#             # rospy.loginfo(self.points[label])
#             response.message = label + " Saved"
#             rospy.loginfo(label + " Position Saved Successfully")
        
#         else:

#             f = open("/home/user/catkin_ws/src/my_turtlebot_localization/text/spots.txt","w")
    
#             for key in self.points:

#                 f.write(str(key) + "\n--------------------------\n" + str(self.points[key]) + "\n--------------------------\n")

#             f.close()

#             response.message = "File Saved Successfully!!!"
#             response.navigation_successfull = True
        
#         return response
            
# if __name__ == '__main__':
#     rospy.init_node('spot_recorder', anonymous=True)
#     spot_object = SaveSpot()
#     rospy.spin() 





