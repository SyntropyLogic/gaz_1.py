from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # --- 1. Start Gazebo with an empty world ---
    start_gazebo_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': '-r empty.sdf'}.items() # Use '-r' to run a world
    )

    # --- 2. Spawn a drone model into the world ---
    # This command uses ros_gz_sim's 'create' service to spawn a model from Gazebo's online library (Fuel)
    spawn_drone_cmd = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'empty',
            '-name', 'x3_quadrotor',
            '-file', 'X3_Sensor_Config_1', # This is a standard model on Gazebo Fuel
            '-x', '0',
            '-y', '0',
            '-z', '0.3'
        ],
        output='screen'
    )
    
    return LaunchDescription([
        start_gazebo_cmd,
        spawn_drone_cmd
    ])
