synergy-logic@synergy-logic-ubuntu:~$ cd ~/usl_drone_project
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ colcon build
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/lib/python3/dist-packages/setuptools/_distutils/core.py", line 267, in run_setup
    exec(code, g)
  File "<string>", line 9, in <module>
ModuleNotFoundError: No module named 'Cython'
[0.620s] ERROR:colcon.colcon_core.package_identification:Exception in package identification extension 'python_setup_py' in 'venv/lib/python3.12/site-packages/numpy/_core/tests/examples/cython': Command '['/usr/bin/python3', '-c', 'import sys;from contextlib import suppress;exec("with suppress(ImportError):    from setuptools.extern.packaging.specifiers    import SpecifierSet");exec("with suppress(ImportError):    from packaging.specifiers import SpecifierSet");from distutils.core import run_setup;dist = run_setup(    \'setup.py\', script_args=(\'--dry-run\',), stop_after=\'config\');skip_keys = (\'cmdclass\', \'distclass\', \'ext_modules\', \'metadata\');data = {    key: value for key, value in dist.__dict__.items()     if (        not key.startswith(\'_\') and         not callable(value) and         key not in skip_keys and         key not in dist.display_option_names    )};data[\'metadata\'] = {    k: v for k, v in dist.metadata.__dict__.items()     if k not in (\'license_files\', \'provides_extras\')};sys.stdout.buffer.write(repr(data).encode(\'utf-8\'))']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/colcon_core/package_identification/__init__.py", line 144, in _identify
    retval = extension.identify(_reused_descriptor_instance)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/colcon_python_setup_py/package_identification/python_setup_py.py", line 48, in identify
    config = get_setup_information(setup_py)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/colcon_python_setup_py/package_identification/python_setup_py.py", line 249, in get_setup_information
    _setup_information_cache[hashable_env] = _get_setup_information(
                                             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/colcon_python_setup_py/package_identification/python_setup_py.py", line 296, in _get_setup_information
    result = subprocess.run(
             ^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/usr/bin/python3', '-c', 'import sys;from contextlib import suppress;exec("with suppress(ImportError):    from setuptools.extern.packaging.specifiers    import SpecifierSet");exec("with suppress(ImportError):    from packaging.specifiers import SpecifierSet");from distutils.core import run_setup;dist = run_setup(    \'setup.py\', script_args=(\'--dry-run\',), stop_after=\'config\');skip_keys = (\'cmdclass\', \'distclass\', \'ext_modules\', \'metadata\');data = {    key: value for key, value in dist.__dict__.items()     if (        not key.startswith(\'_\') and         not callable(value) and         key not in skip_keys and         key not in dist.display_option_names    )};data[\'metadata\'] = {    k: v for k, v in dist.metadata.__dict__.items()     if k not in (\'license_files\', \'provides_extras\')};sys.stdout.buffer.write(repr(data).encode(\'utf-8\'))']' returned non-zero exit status 1.

[0.842s] ERROR:colcon.colcon_core.package_identification:Failed to determine Python package name in 'venv/lib/python3.12/site-packages/numpy/_core/tests/examples/limited_api'
[0.842s] ERROR:colcon.colcon_core.package_identification:Exception in package identification extension 'python_setup_py' in 'venv/lib/python3.12/site-packages/numpy/_core/tests/examples/limited_api': Failed to determine Python package name in 'venv/lib/python3.12/site-packages/numpy/_core/tests/examples/limited_api'
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/colcon_core/package_identification/__init__.py", line 144, in _identify
    retval = extension.identify(_reused_descriptor_instance)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/colcon_python_setup_py/package_identification/python_setup_py.py", line 57, in identify
    raise RuntimeError(
RuntimeError: Failed to determine Python package name in 'venv/lib/python3.12/site-packages/numpy/_core/tests/examples/limited_api'

Starting >>> my-test-package
Starting >>> usl_drone_project
--- stderr: usl_drone_project                                 
error: can't copy 'resource/usl_drone_project': doesn't exist or not a regular file
---
Failed   <<< usl_drone_project [1.19s, exited with code 1]
Aborted  <<< my-test-package [1.20s]                     

Summary: 0 packages finished [2.46s]
  1 package failed: usl_drone_project
  1 package aborted: my-test-package
  1 package had stderr output: usl_drone_project
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ source install/setup.bash
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ ros2 launch usl_drone_project usl_gazebo.launch.py
\Package 'usl_drone_project' not found: "package 'usl_drone_project' not found, searching: ['/opt/ros/jazzy']"
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ source /opt/ros/jazzy/setup.bash
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ source install/setup.bash
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ source ../venv/bin/activate
bash: ../venv/bin/activate: No such file or directory
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ ros2 launch usl_drone_project usl_gazebo.launch.py
Package 'usl_drone_project' not found: "package 'usl_drone_project' not found, searching: ['/opt/ros/jazzy']"
synergy-logic@synergy-logic-ubuntu:~/usl_drone_project$ 
