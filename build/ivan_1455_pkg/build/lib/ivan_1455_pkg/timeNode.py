#!/usr/bin/env python3
"""time node"""

import rclpy
from rclpy.node import Node
import time
from datetime import datetime

class CurrentTimeNode(Node):
    def __init__(self):
        super().__init__('current_time_node')

        self.timer = self.create_timer(5.0, self.timer_callback)
        self. get_logger().info("Njde is activated. Time will be shown every 5 sec.")
    
    def timer_callback(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.get_logger().info(f"Current Time: {formatted_time}")

def main(args=None):
    rclpy.init(args=args)                   # инициализация ROS 2
    node = CurrentTimeNode()               
    ##node.get_logger().info("Hello ROS 2 World! 🚀")
    rclpy.spin(node)                        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()