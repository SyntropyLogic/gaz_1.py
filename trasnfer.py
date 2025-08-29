synergy-logic@synergy-logic-ubuntu:~$ sudo apt install python3-lark python3-packaging python3-catkin-pkg python3-empy python3-numpy python3-transforms3d python3-yaml
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-lark is already the newest version (1.1.9-1).
python3-lark set to manually installed.
python3-packaging is already the newest version (24.0-1).
python3-packaging set to manually installed.
python3-empy is already the newest version (3.3.4-2).
python3-empy set to manually installed.
python3-numpy is already the newest version (1:1.26.4+ds-6ubuntu1).
python3-numpy set to manually installed.
python3-transforms3d is already the newest version (0.4.1+ds-1).
python3-transforms3d set to manually installed.
python3-yaml is already the newest version (6.0.1-2build2).
python3-yaml set to manually installed.
The following NEW packages will be installed:
  python3-catkin-pkg
0 upgraded, 1 newly installed, 0 to remove and 456 not upgraded.
Need to get 3,920 B of archives.
After this operation, 26.6 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://packages.ros.org/ros2/ubuntu noble/main amd64 python3-catkin-pkg all 1.0.0-100 [3,920 B]
Fetched 3,920 B in 2s (2,345 B/s)              
Selecting previously unselected package python3-catkin-pkg.
(Reading database ... 372310 files and directories currently installed.)
Preparing to unpack .../python3-catkin-pkg_1.0.0-100_all.deb ...
Unpacking python3-catkin-pkg (1.0.0-100) ...
Setting up python3-catkin-pkg (1.0.0-100) ...
synergy-logic@synergy-logic-ubuntu:~$ cd ~/usl_drone_project
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ rm -rf build install log 
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ colcon build
Starting >>> intent_msgs
Starting >>> usl_drone_project
Finished <<< usl_drone_project [1.26s]                          
--- stderr: intent_msgs                             
CMake Warning:
  Manually-specified variables were not used by the project:

    CATKIN_INSTALL_INTO_PREFIX_ROOT


---
Finished <<< intent_msgs [4.49s]

Summary: 2 packages finished [4.78s]
  1 package had stderr output: intent_msgs
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ source install/setup.bash
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ ros2 launch usl_drone_project usl_gazebo.launch.py
Package 'usl_drone_project' not found: "package 'usl_drone_project' not found, searching: ['/opt/ros/jazzy']"
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ 
