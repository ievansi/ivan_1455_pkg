
#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ivan_1455_pkg',           # ← замени на своё имя пакета
            executable='even_number_publisher',
            name='even_pub',
            output='screen',
        ),
        Node(
            package='ivan_1455_pkg',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
        ),
    ])