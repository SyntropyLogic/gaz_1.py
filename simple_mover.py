import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy

# --- The Topic for the Diff Drive Demo Robot ---
# Remember to run 'ros2 topic list' to confirm this if needed!
CMD_VEL_TOPIC = '/diff_drive/cmd_vel' 

class SimpleMoverNode(Node):
    def __init__(self):
        super().__init__('simple_mover_node')

        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.VOLATILE,
            depth=10
        )

        self.publisher_ = self.create_publisher(Twist, CMD_VEL_TOPIC, qos_profile)
        self.timer = self.create_timer(0.1, self.publish_command)
        
        self.get_logger().info('Simple Mover Node has started.')
        self.get_logger().info(f'--> Publishing forward command to {CMD_VEL_TOPIC}...')

    def publish_command(self):
        # Move forward at 0.5 m/s
        twist_msg = Twist(linear=Vector3(x=0.5, y=0.0, z=0.0))
        self.publisher_.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    simple_mover_node = SimpleMoverNode()
    try:
        rclpy.spin(simple_mover_node)
    except KeyboardInterrupt:
        pass
    finally:
        simple_mover_node.get_logger().info('Stopping robot...')
        simple_mover_node.publisher_.publish(Twist())
        simple_mover_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
