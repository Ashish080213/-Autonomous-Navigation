#!/usr/bin/env python               

import rospy
import os
from nav_msgs.msg import OccupancyGrid   # OcuupancyGrid represents the occupancy grid maps

def automatic_map_saver():
    rospy.init_node('automatic_map_saver', anonymous=True)

    rospy.loginfo('Waiting for the map to be available...')
    rospy.wait_for_message('/map', OccupancyGrid)
    rospy.loginfo('Map received.')


    rospy.loginfo('Press "S" to save the map...')
    while True:
        user_input = input()
        if user_input.lower() == 's':
            break


    map_file_path = os.path.expanduser('~/catkin_ws/src/my_turtlebot_mapping/maps/my_map')
    map_saver_command = 'rosrun map_server map_saver -f {}'.format(map_file_path)
    
    # executes the 'map_saver' command using the 'os.system' function
    os.system(map_saver_command)

    rospy.loginfo('Map saved to: %s' % map_file_path)

if __name__ == '__main__':
    try:
        automatic_map_saver()
    except rospy.ROSInterruptException:
        pass
