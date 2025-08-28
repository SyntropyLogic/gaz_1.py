



synergy-logic@synergy-logic-ubuntu:~$ sudo apt install software-properties-common -y
[sudo] password for synergy-logic: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-software-properties software-properties-gtk
The following packages will be upgraded:
  python3-software-properties software-properties-common
  software-properties-gtk
3 upgraded, 0 newly installed, 0 to remove and 456 not upgraded.
Need to get 128 kB of archives.
After this operation, 0 B of additional disk space will be used.
Get:1 http://au.archive.ubuntu.com/ubuntu noble-updates/main amd64 software-properties-common all 0.99.49.3 [14.4 kB]
Get:2 http://au.archive.ubuntu.com/ubuntu noble-updates/main amd64 software-properties-gtk all 0.99.49.3 [83.2 kB]
Get:3 http://au.archive.ubuntu.com/ubuntu noble-updates/main amd64 python3-software-properties all 0.99.49.3 [29.9 kB]
Fetched 128 kB in 0s (562 kB/s)                       
(Reading database ... 372289 files and directories currently installed.)
Preparing to unpack .../software-properties-common_0.99.49.3_all.d
eb ...
Unpacking software-properties-common (0.99.49.3) over (0.99.49.2) 
...
Preparing to unpack .../software-properties-gtk_0.99.49.3_all.deb 
...
Unpacking software-properties-gtk (0.99.49.3) over (0.99.49.2) ...
Preparing to unpack .../python3-software-properties_0.99.49.3_all.
deb ...
Unpacking python3-software-properties (0.99.49.3) over (0.99.49.2)
 ...
Setting up python3-software-properties (0.99.49.3) ...
Setting up software-properties-common (0.99.49.3) ...
Setting up software-properties-gtk (0.99.49.3) ...
Processing triggers for libglib2.0-0t64:amd64 (2.80.0-6ubuntu3.4) 
...
Processing triggers for dbus (1.14.10-4ubuntu4.1) ...
Processing triggers for shared-mime-info (2.4-4) ...
Processing triggers for desktop-file-utils (0.27-2build1) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for gnome-menus (3.36.0-1.1ubuntu3) ...
Processing triggers for man-db (2.12.0-4build2) ...
synergy-logic@synergy-logic-ubuntu:~$ sudo add-apt-repository universe -y
Adding component(s) 'universe' to all repositories.
Hit:1 http://au.archive.ubuntu.com/ubuntu noble InRelease
Hit:2 http://au.archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:3 https://brave-browser-apt-release.s3.brave.com stable InRelease
Hit:4 http://au.archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:5 https://packages.microsoft.com/repos/code stable InRelease 
Hit:6 http://packages.osrfoundation.org/gazebo/ubuntu-stable noble InRelease
Hit:7 http://packages.ros.org/ros2/ubuntu noble InRelease        
Hit:8 http://security.ubuntu.com/ubuntu noble-security InRelease
Reading package lists... Done
synergy-logic@synergy-logic-ubuntu:~$ sudo apt update && sudo apt install curl -y
Hit:1 http://au.archive.ubuntu.com/ubuntu noble InRelease
Hit:2 https://brave-browser-apt-release.s3.brave.com stable InRelease
Hit:3 http://au.archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:4 http://au.archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:5 https://packages.microsoft.com/repos/code stable InRelease 
Hit:6 http://packages.osrfoundation.org/gazebo/ubuntu-stable noble InRelease
Hit:7 http://packages.ros.org/ros2/ubuntu noble InRelease        
Hit:8 http://security.ubuntu.com/ubuntu noble-security InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
456 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
curl is already the newest version (8.5.0-2ubuntu10.6).
0 upgraded, 0 newly installed, 0 to remove and 456 not upgraded.
synergy-logic@synergy-logic-ubuntu:~$ sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
synergy-logic@synergy-logic-ubuntu:~$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
synergy-logic@synergy-logic-ubuntu:~$ sudo apt update
Hit:1 http://au.archive.ubuntu.com/ubuntu noble InRelease
Hit:2 https://brave-browser-apt-release.s3.brave.com stable InRelease
Hit:3 http://au.archive.ubuntu.com/ubuntu noble-updates InRelease
Hit:4 http://au.archive.ubuntu.com/ubuntu noble-backports InRelease
Hit:5 https://packages.microsoft.com/repos/code stable InRelease 
Hit:6 http://packages.osrfoundation.org/gazebo/ubuntu-stable noble InRelease
Hit:7 http://packages.ros.org/ros2/ubuntu noble InRelease        
Hit:8 http://security.ubuntu.com/ubuntu noble-security InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
456 packages can be upgraded. Run 'apt list --upgradable' to see them.
synergy-logic@synergy-logic-ubuntu:~$ sudo apt install ros-jazzy-gazebo-ros-pkgs
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Package ros-jazzy-gazebo-ros-pkgs is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'ros-jazzy-gazebo-ros-pkgs' has no installation candidate
synergy-logic@synergy-logic-ubuntu:~$ 
