import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy

# --- The Correct Topic Name for the PX4 Drone in Gazebo ---
CMD_VEL_TOPIC = '/drone/cmd_vel' 
