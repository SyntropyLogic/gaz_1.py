import os
import sys
import launch
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # This finds the path to the 'ros_gz_sim_demos' package you installed
    pkg_ros_gz_sim_demos = get_package_share_directory('ros_gz_sim_demos')

    # This is the full path to a world file that is guaranteed to be on your computer
    world_file_path = os.path.join(pkg_ros_gz_sim_demos, 'worlds', 'multicopter.sdf')

    # This command will launch Gazebo and tell it to load our local world file
    start_gazebo_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': world_file_path}.items()
    )

    return LaunchDescription([
        start_gazebo_cmd,
    ])

# --- THIS IS THE NEW CODE BLOCK ---
# This block allows the launch file to be executed directly with 'python3'
if __name__ == '__main__':
    ld = generate_launch_description()
    ls = launch.LaunchService(argv=sys.argv[1:])
    ls.include_launch_description(ld)
    sys.exit(ls.run())
