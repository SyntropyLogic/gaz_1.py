from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # This is the most basic command to start Gazebo.
    # It will open a Gazebo window with a ground plane and a sun.
    start_gazebo_cmd = Node(
        package='ros_gz_sim',
        executable='gz_sim',
        arguments=['-r', 'empty.sdf'], # '-r' means run, 'empty.sdf' is a built-in empty world
        output='screen'
    )

    return LaunchDescription([
        start_gazebo_cmd,
    ])
