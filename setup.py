from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'usl_drone_project'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/''/' + package_name, ['package.xml']),
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
            'usl_main = usl_drone_project.main:main',
            'usl_command_gate = usl_drone_project.command_gate:main',
            'usl_adaptive_controller = usl_drone_project.adaptive_controller:main',
            'usl_intent_translator = usl_drone_project.intent_translator:main',
            'usl_mission = usl_drone_project.entropic_mission_ena:main',
            'usl_simple_mover = usl_drone_project.simple_mover:main',
        ],
    },
)
