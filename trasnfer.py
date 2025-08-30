
synergy-logic@synergy-logic-ubuntu:~/usl_workspace$ colcon --log-level debug build
DEBUG:colcon:Parsed command line arguments: Namespace(log_base=None, log_level=10, verb_name='build', build_base='build', install_base='install', merge_install=False, symlink_install=False, test_result_base=None, continue_on_error=False, executor='parallel', parallel_workers=16, event_handlers=None, ignore_user_meta=False, metas=['./colcon.meta'], base_paths=['.'], packages_ignore=None, packages_ignore_regex=None, paths=None, packages_up_to=None, packages_up_to_regex=None, packages_above=None, packages_above_and_dependencies=None, packages_above_depth=None, packages_select_by_dep=None, packages_skip_by_dep=None, packages_skip_up_to=None, packages_select_build_failed=False, packages_skip_build_finished=False, packages_select_test_failures=False, packages_skip_test_passed=False, packages_select=None, packages_skip=None, packages_select_regex=None, packages_skip_regex=None, packages_start=None, packages_end=None, allow_overriding=[], cmake_args=None, cmake_target=None, cmake_target_skip_unavailable=False, cmake_clean_cache=False, cmake_clean_first=False, cmake_force_configure=False, ament_cmake_args=None, catkin_cmake_args=None, catkin_skip_building_tests=False, verb_parser=<colcon_defaults.argument_parser.defaults.DefaultArgumentsDecorator object at 0x74021e94d430>, verb_extension=<colcon_core.verb.build.BuildVerb object at 0x74021e94d310>, main=<bound method BuildVerb.main of <colcon_core.verb.build.BuildVerb object at 0x74021e94d310>>)
INFO:colcon.colcon_core.location:Using log path 'log/build_2025-08-30_10-48-30'
[0.116s] INFO:colcon.colcon_core.package_discovery:Crawling recursively for packages in '/home/synergy-logic/usl_workspace'
[0.141s] DEBUG:colcon.colcon_core.package_identification:Package 'src/intent_msgs' with type 'ros.catkin' and name 'intent_msgs'
[0.142s] DEBUG:colcon.colcon_core.package_identification:Package 'src/usl_drone_project' with type 'ros.ament_python' and name 'usl_drone_project'
[0.160s] DEBUG:colcon.colcon_core.verb:Building package 'intent_msgs' with the following arguments: {'ament_cmake_args': None, 'build_base': '/home/synergy-logic/usl_workspace/build/intent_msgs', 'catkin_cmake_args': None, 'catkin_skip_building_tests': False, 'cmake_args': None, 'cmake_clean_cache': False, 'cmake_clean_first': False, 'cmake_force_configure': False, 'cmake_target': None, 'cmake_target_skip_unavailable': False, 'install_base': '/home/synergy-logic/usl_workspace/install/intent_msgs', 'merge_install': False, 'path': '/home/synergy-logic/usl_workspace/src/intent_msgs', 'symlink_install': False, 'test_result_base': None}
[0.161s] DEBUG:colcon.colcon_core.verb:Building package 'usl_drone_project' with the following arguments: {'ament_cmake_args': None, 'build_base': '/home/synergy-logic/usl_workspace/build/usl_drone_project', 'catkin_cmake_args': None, 'catkin_skip_building_tests': False, 'cmake_args': None, 'cmake_clean_cache': False, 'cmake_clean_first': False, 'cmake_force_configure': False, 'cmake_target': None, 'cmake_target_skip_unavailable': False, 'install_base': '/home/synergy-logic/usl_workspace/install/usl_drone_project', 'merge_install': False, 'path': '/home/synergy-logic/usl_workspace/src/usl_drone_project', 'symlink_install': False, 'test_result_base': None}
[0.161s] INFO:colcon.colcon_core.executor:Executing jobs using 'parallel' executor
[0.161s] DEBUG:colcon.colcon_parallel_executor.executor.parallel:run_until_complete
[0.162s] INFO:colcon.colcon_ros.task.catkin.build:Building ROS package in '/home/synergy-logic/usl_workspace/src/intent_msgs' with build type 'catkin'
[0.162s] INFO:colcon.colcon_cmake.task.cmake.build:Building CMake package in '/home/synergy-logic/usl_workspace/src/intent_msgs'
Starting >>> intent_msgs
[0.164s] INFO:colcon.colcon_core.plugin_system:Skipping extension 'colcon_core.shell.bat': Not used on non-Windows systems
[0.164s] INFO:colcon.colcon_core.shell:Skip shell extension 'powershell' for command environment: Not usable outside of PowerShell
[0.164s] DEBUG:colcon.colcon_core.shell:Skip shell extension 'dsv' for command environment
[0.169s] DEBUG:colcon.colcon_core.event_handler.log_command:Invoking command in '/home/synergy-logic/usl_workspace/build/intent_msgs': DEBUGINFOD_URLS=https://debuginfod.ubuntu.com /usr/bin/cmake /home/synergy-logic/usl_workspace/src/intent_msgs -DCATKIN_INSTALL_INTO_PREFIX_ROOT=0 -DCMAKE_INSTALL_PREFIX=/home/synergy-logic/usl_workspace/install/intent_msgs
[0.481s] DEBUG:colcon.colcon_core.event_handler.log_command:Invoked command in '/home/synergy-logic/usl_workspace/build/intent_msgs' returned '1': DEBUGINFOD_URLS=https://debuginfod.ubuntu.com /usr/bin/cmake /home/synergy-logic/usl_workspace/src/intent_msgs -DCATKIN_INSTALL_INTO_PREFIX_ROOT=0 -DCMAKE_INSTALL_PREFIX=/home/synergy-logic/usl_workspace/install/intent_msgs
[0.497s] INFO:colcon.colcon_core.shell:Creating package script '/home/synergy-logic/usl_workspace/install/intent_msgs/share/intent_msgs/package.ps1'
[0.498s] INFO:colcon.colcon_core.shell:Creating package descriptor '/home/synergy-logic/usl_workspace/install/intent_msgs/share/intent_msgs/package.dsv'
[0.498s] INFO:colcon.colcon_core.shell:Creating package script '/home/synergy-logic/usl_workspace/install/intent_msgs/share/intent_msgs/package.sh'
[0.499s] INFO:colcon.colcon_core.shell:Creating package script '/home/synergy-logic/usl_workspace/install/intent_msgs/share/intent_msgs/package.bash'
[0.499s] INFO:colcon.colcon_core.shell:Creating package script '/home/synergy-logic/usl_workspace/install/intent_msgs/share/intent_msgs/package.zsh'
--- stderr: intent_msgs
CMake Error at CMakeLists.txt:9 (find_package):
  By not providing "Findament_cmake.cmake" in CMAKE_MODULE_PATH this project
  has asked CMake to find a package configuration file provided by
  "ament_cmake", but CMake did not find one.

  Could not find a package configuration file provided by "ament_cmake" with
  any of the following names:

    ament_cmakeConfig.cmake
    ament_cmake-config.cmake

  Add the installation prefix of "ament_cmake" to CMAKE_PREFIX_PATH or set
  "ament_cmake_DIR" to a directory containing one of the above files.  If
  "ament_cmake" provides a separate development package or SDK, be sure it
  has been installed.


---
Failed   <<< intent_msgs [0.34s, exited with code 1]
[0.510s] DEBUG:colcon.colcon_parallel_executor.executor.parallel:closing loop
[0.511s] DEBUG:colcon.colcon_parallel_executor.executor.parallel:loop closed
[0.511s] DEBUG:colcon.colcon_parallel_executor.executor.parallel:run_until_complete finished with '1'
[0.511s] DEBUG:colcon.colcon_core.event_reactor:joining thread

Summary: 0 packages finished [0.44s]
  1 package failed: intent_msgs
  1 package had stderr output: intent_msgs
  1 package not processed
[0.516s] INFO:colcon.colcon_core.plugin_system:Skipping extension 'colcon_notification.desktop_notification.terminal_notifier': Not used on non-Darwin systems
[0.516s] INFO:colcon.colcon_core.plugin_system:Skipping extension 'colcon_notification.desktop_notification.win32': Not used on non-Windows systems
[0.516s] INFO:colcon.colcon_notification.desktop_notification:Sending desktop notification using 'notify2'
[0.527s] DEBUG:colcon.colcon_core.event_reactor:joined thread
[0.527s] INFO:colcon.colcon_core.shell:Creating prefix script '/home/synergy-logic/usl_workspace/install/local_setup.ps1'
[0.528s] INFO:colcon.colcon_core.shell:Creating prefix util module '/home/synergy-logic/usl_workspace/install/_local_setup_util_ps1.py'
[0.529s] INFO:colcon.colcon_core.shell:Creating prefix chain script '/home/synergy-logic/usl_workspace/install/setup.ps1'
[0.530s] INFO:colcon.colcon_core.shell:Creating prefix script '/home/synergy-logic/usl_workspace/install/local_setup.sh'
[0.530s] INFO:colcon.colcon_core.shell:Creating prefix util module '/home/synergy-logic/usl_workspace/install/_local_setup_util_sh.py'
[0.531s] INFO:colcon.colcon_core.shell:Creating prefix chain script '/home/synergy-logic/usl_workspace/install/setup.sh'
[0.532s] INFO:colcon.colcon_core.shell:Creating prefix script '/home/synergy-logic/usl_workspace/install/local_setup.bash'
[0.532s] INFO:colcon.colcon_core.shell:Creating prefix chain script '/home/synergy-logic/usl_workspace/install/setup.bash'
[0.532s] INFO:colcon.colcon_core.shell:Creating prefix script '/home/synergy-logic/usl_workspace/install/local_setup.zsh'
[0.533s] INFO:colcon.colcon_core.shell:Creating prefix chain script '/home/synergy-logic/usl_workspace/install/setup.zsh'
synergy-logic@synergy-logic-ubuntu:~/usl_workspace$ 
