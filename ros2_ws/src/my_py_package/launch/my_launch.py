import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # 获取包的安装路径
    pkg_share = get_package_share_directory("my_py_package")
    # 构建参数文件的完整路径
    params_file = os.path.join(pkg_share, "config", "params.yaml")

    # 启动 talker 节点，加载参数文件
    talker_node = Node(
        package="my_py_package",
        executable="talker",
        name="talker",
        parameters=[params_file],
    )

    # 启动 listener 节点，加载参数文件（也可以单独指定参数，这里演示共用文件）
    listener_node = Node(
        package="my_py_package",
        executable="listener",
        name="listener",
        parameters=[params_file],
    )

    return LaunchDescription([talker_node, listener_node])
