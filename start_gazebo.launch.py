import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Get the launch directory for the PX4 simulation
    px4_simulation_dir = get_package_share_directory('px4_simulation')

    # Include the main launch file from the PX4 simulation package
    # This will start Gazebo, spawn the drone, and start the PX4 flight controller
    start_px4_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(px4_simulation_dir, 'launch', 'gazebo_iris.launch.py')
        )
    )

    return LaunchDescription([
        start_px4_cmd
    ])
