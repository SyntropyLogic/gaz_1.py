

blue boxc didint move to ensure ive done it right heres topic list and simple-mover im running 

synergy-logic@synergy-logic-ubuntu:~$ ros2 topic list
/clicked_point
/initialpose
/model/vehicle_blue/cmd_vel
/model/vehicle_blue/odometry
/model/vehicle_green/cmd_vel
/model/vehicle_green/odometry
/move_base_simple/goal
/parameter_events
/rosout
/tf
/tf_static
synergy-logic@synergy-logic-ubuntu:~$ 



import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy

# --- The Correct Topic Name for the Diff Drive Demo Robot ---
CMD_VEL_TOPIC = '/vehicle_blue/cmd_vel' 

class SimpleMoverNode(Node):
    def __init__(self):
        super().__init__('simple_mover_node')

        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.VOLATILE,
            depth=10
        )

        self.publisher_ = self.create_publisher(Twist, CMD_VEL_TOPIC, qos_profi>
        self.timer = self.create_timer(0.1, self.publish_command)
                               [ Read 44 lines ]
^G Help      ^O Write Out ^W Where Is  ^K Cut       ^T Execute   ^C Location
^X Exit      ^R Read File ^\ Replace   ^U Paste     ^J Justify   ^/ Go To Line




