import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/igsp-01/ros2_ws/src/ivan_1455_pkg/install/ivan_1455_pkg'
