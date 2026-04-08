#!/usr/bin/env python3
import rclpy                        # главная библиотека ROS 2
from rclpy.node import Node         # от неё наследуемся
from std_msgs.msg import Int32     # тип сообщения 

class EvenNumberPublisher(Node):

    def __init__(self):
        # Даём узлу
        super().__init__('even_pub')

         # Объявляем параметры с значениями по умолчанию
        self.declare_parameter('publish_frequency', 10.0)   # Гц
        self.declare_parameter('overflow_threshold', 100)
        self.declare_parameter('topic_name', 'even_numbers')
        self.declare_parameter('overflow_topic', 'overflow')

        # Читаем их
        self.freq = self.get_parameter('publish_frequency').value
        self.threshold = self.get_parameter('overflow_threshold').value
        self.topic = self.get_parameter('topic_name').value
        self.overflow_topic = self.get_parameter('overflow_topic').value

        self.publisher = self.create_publisher(Int32, self.topic_name, 10) #публикатор четных чисел
        self.overflow_publisher = self.create_publisher(Int32, self.overflow_topic, 10) #публикотор переполнения
        
        stimer_period = 1.0 / self.freq
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.even_number = 0

        self.get_logger().info("=" * 50)
        self.get_logger().info("Публикатор чётных чисел запущен")
        self.get_logger().info(f"  - Частота: {self.freq} Гц")
        self.get_logger().info(f"  - Порог переполнения: {self.threshold}")
        self.get_logger().info(f"  - Топик чисел: {self.topic_name}")
        self.get_logger().info(f"  - Топик переполнения: {self.overflow_topic}")
        self.get_logger().info("=" * 50)

  
    def timer_callback(self):
        if self.even_number >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.even_number
            self.overflow_publisher.publish(overflow_msg)

            self.get_logger().warn(f"ПЕРЕПОЛНЕНИЕ! Значение {self.even_number}  отправлено в топик /overflow")
            self.even_number = 0
        
        msg = Int32()
        msg.data = self.even_number
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {self.even_number}")
        self.even_number += 2

def main():
    rclpy.init()                    # стартуем ROS 2
    node = EvenNumberPublisher()               # создаём наш узел
    try:
        rclpy.spin(node)            # крутимся и ждём сообщений
    except KeyboardInterrupt:
        node.get_logger().info("Node stopped by user")                      # Ctrl+C — нормально выходим
    finally:
        node.destroy_node()         # убираем узел
        rclpy.shutdown()            # завершаем ROS 2

if __name__ == '__main__':
    main()