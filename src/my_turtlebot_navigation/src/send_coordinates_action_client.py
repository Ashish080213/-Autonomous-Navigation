#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import time
import math
import actionlib


class SendCoordinates():
    
    def __init__(self, label, goalpoint):

        rospy.loginfo("calling movebase_action....")
        self.goalpoint = goalpoint
        self.flag = False
        rospy.on_shutdown(self.shutdownhook)

        client = actionlib.SimpleActionClient("/move_base", MoveBaseAction)

        goal = MoveBaseGoal()
        temp_goal = Pose()

        tag = label
        self.rate = rospy.Rate(10)

        while not self.flag:
            goal.target_pose.header.frame_id = "map"
            temp_goal.position.x = goalpoint['position']['x']
            temp_goal.position.y = goalpoint['position']['y']
            temp_goal.position.z = goalpoint['position']['z']
            temp_goal.orientation.x = goalpoint['orientation']['x']
            temp_goal.orientation.y = goalpoint['orientation']['y']
            temp_goal.orientation.z = goalpoint['orientation']['z']
            temp_goal.orientation.w = goalpoint['orientation']['w']
            goal.target_pose.pose = temp_goal
        
            client.wait_for_server()
            client.send_goal(goal, feedback_cb=self.feedback_callback)
            client.wait_for_result()
            result = client.get_state()

            if result == 3:
                print("Successfully Reached Goal")
                self.shutdownhook()



    def shutdownhook(self):
        self.flag = True
        rospy.loginfo("Shutting down")

 
    def feedback_callback(self, data):
        return
        
            
if __name__ == '__main__':

    rospy.init_node('send_coordinates_node', anonymous=True)
    rospy.spin()


