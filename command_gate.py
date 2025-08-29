import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.executors import MultiThreadedExecutor
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy

# --- The Correct Topic for our Spawned X3 Drone ---
FINAL_CMD_VEL_TOPIC = '/x3_quadrotor/cmd_vel'

class CommandGate(Node):
    def __init__(self):
        super().__init__('command_gate')
        
        # Define the robust QoS profile we know works
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            durability=QoSDurabilityPolicy.VOLATILE,
            depth=10
        )
        
        self.cmd_vel_publisher = self.create_publisher(Twist, FINAL_CMD_VEL_TOPIC, qos_profile)
        
        self.mission_subscriber = self.create_subscription(
            Twist, '/mission_cmd', self.mission_callback, 10)
        self.correction_subscriber = self.create_subscription(
            Twist, '/correction_cmd', self.correction_callback, 10)
            
        # --- State Flags and Timers ---
        self.is_correcting = False
        self.on_cooldown = False
        self.correction_pulse_timer = None
        self.cooldown_timer = None

        # --- Dynamic Cooldown Parameters ---
        self.base_cooldown_sec = 0.5
        self.cooldown_scaling_factor = 4.0

        self.get_logger().info('Command Gate node initialized.')
        self.get_logger().info(f'--> Forwarding final commands to {FINAL_CMD_VEL_TOPIC}')

    def mission_callback(self, msg):
        if not self.is_correcting:
            self.cmd_vel_publisher.publish(msg)

    def correction_callback(self, msg):
        if self.on_cooldown:
            return

        self.is_correcting = True
        self.on_cooldown = True

        drift_delta = msg.angular.z
        cooldown_duration = min(self.base_cooldown_sec + (drift_delta * self.cooldown_scaling_factor), 5.0)

        correction_twist = Twist()
        correction_twist.angular.x = msg.angular.x
        correction_twist.angular.y = msg.angular.y
        
        self.cmd_vel_publisher.publish(correction_twist)
        
        self.correction_pulse_timer = self.create_timer(0.2, self.end_correction_pulse)
        self.cooldown_timer = self.create_timer(cooldown_duration, self.end_cooldown_period)

    def end_correction_pulse(self):
        self.cmd_vel_publisher.publish(Twist()) # Send stop command
        self.is_correcting = False
        if self.correction_pulse_timer: self.correction_pulse_timer.cancel()

    def end_cooldown_period(self):
        self.on_cooldown = False
        if self.cooldown_timer: self.cooldown_timer.cancel()

# --- Main function remains the same ---
def main(args=None):
    rclpy.init(args=args)
    command_gate_node = CommandGate()
    executor = MultiThreadedExecutor()
    executor.add_node(command_gate_node)
    try:
        executor.spin()
    finally:
        executor.shutdown()
        command_gate_node.destroy_node()

if __name__ == '__main__':
    main()
