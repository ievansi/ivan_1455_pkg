#!/usr/bin/env python3
import rclpy                        # главная библиотека ROS 2
from rclpy.node import Node         # от неё наследуемся
from std_msgs.msg import Int32     # тип сообщения 

class EvenNumberPublisher(Node):

    def __init__(self):
        # Даём узлу
        super().__init__('even_pub')
        self.publisher = self.create_publisher(Int32, '/even_numbers', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.even_number = 0
        self.get_logger().info("Even numbers puplisher is launched (10 Hz)")

  
    def timer_callback(self):
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