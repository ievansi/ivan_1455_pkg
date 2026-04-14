#!/usr/bin/env python3
import rclpy                        # главная библиотека ROS 2
from rclpy.node import Node         # от неё наследуемся
from std_msgs.msg import Int32     # тип сообщения 

class OverflowListener(Node):

    def __init__(self):
        # Даём узлу
        super().__init__('overflow_listener')

        # Объявляем параметры
        self.declare_parameter('overflow_topic', 'overflow')
        
        # Читаем параметры
        self.overflow_topic = self.get_parameter('overflow_topic').value
        

        self.subscription = self.create_subscription(
            Int32,
            self.overflow_topic,
            self.callback,
            10
        )
        self.get_logger().info(f"Слушатель запущен. Слушает топик: {self.overflow_topic}")

    def callback(self, msg):
        self.get_logger().warn(f"ПЕРЕПОЛНЕНИЕ! Получено значение {msg.data}")


def main():
    rclpy.init()                    # стартуем ROS 2
    node = OverflowListener()               # создаём наш узел
    try:
        rclpy.spin(node)            # крутимся и ждём сообщений
    except KeyboardInterrupt:
        node.get_logger().info("Node stopped by user")                      # Ctrl+C — нормально выходим
    finally:
        node.destroy_node()         # убираем узел
        rclpy.shutdown()            # завершаем ROS 2

if __name__ == '__main__':
    main()