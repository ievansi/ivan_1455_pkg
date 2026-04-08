#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    
    # ============================================
    # 1. ОБЪЯВЛЯЕМ АРГУМЕНТЫ (можно менять при запуске)
    # ============================================
    
    freq_arg = DeclareLaunchArgument(
        'publish_frequency',
        default_value='8.0',
        description='Частота публикации чётных чисел (Гц)'
    )
    
    threshold_arg = DeclareLaunchArgument(
        'overflow_threshold',
        default_value='80',
        description='Порог, после которого происходит переполнение'
    )
    
    topic_arg = DeclareLaunchArgument(
        'topic_name',
        default_value='even_numbers',
        description='Имя топика для публикации чётных чисел'
    )
    
    overflow_topic_arg = DeclareLaunchArgument(
        'overflow_topic',
        default_value='overflow',
        description='Имя топика для сообщений о переполнении'
    )
    
    
    # ============================================
    # 2. ПОЛУЧАЕМ ЗНАЧЕНИЯ АРГУМЕНТОВ
    # ============================================
    
    frequency = LaunchConfiguration('publish_frequency')
    threshold = LaunchConfiguration('overflow_threshold')
    topic_name = LaunchConfiguration('topic_name')
    overflow_topic = LaunchConfiguration('overflow_topic')
    
    # ============================================
    # 3. ОПИСЫВАЕМ УЗЛЫ
    # ============================================
    
    # Узел-публикатор чётных чисел
    even_publisher_node = Node(
        package='ivan_1455_pkg',  # ЗАМЕНИТЕ на имя вашего пакета!
        executable='even_number_publisher',
        name='even_pub',
        output='screen',  # Выводить логи в терминал
        parameters=[
            {'publish_frequency': frequency},
            {'overflow_threshold': threshold},
            {'topic_name': topic_name},
            {'overflow_topic': overflow_topic},
        ]
    )
    
    # Узел-слушатель переполнения
    overflow_listener_node = Node(
        package='ivan_1455_pkg',  # ЗАМЕНИТЕ на имя вашего пакета!
        executable='overflow_listener',
        name='overflow_listener',
        output='screen',
        parameters=[
            {'overflow_topic': overflow_topic},
        ]
    )
    
    # ============================================
    # 4. ВОЗВРАЩАЕМ LAUNCHDESCRIPTION
    # ============================================
    
    return LaunchDescription([
        freq_arg,
        threshold_arg,
        topic_arg,
        overflow_topic_arg,
        even_publisher_node,
        overflow_listener_node,
    ])