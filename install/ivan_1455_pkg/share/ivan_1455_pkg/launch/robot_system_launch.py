#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration

def launch_setup(context, *args, **kwargs):
    """
    Эта функция вызывается во время запуска и получает доступ
    к реальным значениям аргументов.
    """
    # Получаем значение аргумента mode
    mode = LaunchConfiguration('mode').perform(context)
    
    # Устанавливаем параметры по умолчанию для выбранного режима
    if mode == 'fast':
        default_freq = 20.0
        default_threshold = 50
        default_topic = '/even_numbers_fast'
    else:  # 'slow' или любое другое значение
        default_freq = 5.0
        default_threshold = 150
        default_topic = '/even_numbers_slow'
    
   
    freq_str = LaunchConfiguration('publish_frequency').perform(context)
    if freq_str == '':  # не задан явно
        freq_value = default_freq
    else:
        freq_value = float(freq_str)
    
    threshold_str = LaunchConfiguration('overflow_threshold').perform(context)
    if threshold_str == '':
        threshold_value = default_threshold
    else:
        threshold_value = int(threshold_str)
    
    topic_str = LaunchConfiguration('topic_name').perform(context)
    if topic_str == '':
        topic_value = default_topic
    else:
        topic_value = topic_str
    
    overflow_topic = LaunchConfiguration('overflow_topic').perform(context)
    if overflow_topic == '':
        overflow_topic = 'overflow'

    even_publisher_node = Node(
        package='ivan_1455_pkg',
        executable='even_number_publisher',
        name='even_pub',
        output='screen',
        parameters=[{
            'publish_frequency': freq_value,
            'overflow_threshold': threshold_value,
            'topic_name': topic_value,
            'overflow_topic': overflow_topic,
        }]
    )
    
    overflow_listener_node = Node(
        package='ivan_1455_pkg',
        executable='overflow_listener',
        name='overflow_listener',
        output='screen',
        parameters=[{
            'overflow_topic': overflow_topic,
        }]
    )
    
    return [even_publisher_node, overflow_listener_node]    

def generate_launch_description():

    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='slow',
        description='Режим работы: fast (20 Гц, порог 50, топик /even_numbers_fast) или slow (5 Гц, порог 150, топик /even_numbers_slow)'
    )

    freq_arg = DeclareLaunchArgument(
        'publish_frequency',
        default_value='',
        description='Частота публикации чётных чисел (Гц)'
    )
    
    threshold_arg = DeclareLaunchArgument(
        'overflow_threshold',
        default_value='',
        description='Порог, после которого происходит переполнение'
    )
    
    topic_arg = DeclareLaunchArgument(
        'topic_name',
        default_value='',
        description='Имя топика для публикации чётных чисел'
    )
    
    overflow_topic_arg = DeclareLaunchArgument(
        'overflow_topic',
        default_value='overflow',
        description='Имя топика для сообщений о переполнении'
    )
    
    
    launch_setup_action = OpaqueFunction(function=launch_setup)
    
    return LaunchDescription([
        mode_arg,
        freq_arg,
        threshold_arg,
        topic_arg,
        overflow_topic_arg,
        launch_setup_action,
    ])