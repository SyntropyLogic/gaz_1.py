from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'usl_drone_project'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']), # Automatically find packages in src
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Crispy',
    maintainer_email='user@todo.todo',
    description='Unified Synergy Logic (USL) Drone Controller',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'executable_name = src_folder.file_name:main'
            'usl_main = src.main:main',
            'usl_command_gate = src.command_gate:main',
            'usl_adaptive_controller = src.adaptive_controller:main',
            'usl_intent_translator = src.intent_translator:main',
            'usl_mission = src.entropic_mission_ena:main',
            'usl_simple_mover = src.simple_mover:main',
        ],
    },
)
