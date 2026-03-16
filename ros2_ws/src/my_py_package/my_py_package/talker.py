import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        # 声明参数，并提供默认值
        self.declare_parameter("publish_rate", 1.0)  # Hz
        self.declare_parameter("topic", "chatter")
        self.declare_parameter("message_prefix", "Hello World")

        # 获取参数值
        publish_rate = (
            self.get_parameter("publish_rate").get_parameter_value().double_value
        )
        topic = self.get_parameter("topic").get_parameter_value().string_value
        self.message_prefix = (
            self.get_parameter("message_prefix").get_parameter_value().string_value
        )

        self.publisher_ = self.create_publisher(String, topic, 10)
        timer_period = 1.0 / publish_rate
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info(
            f'Talker started on topic "{topic}" with rate {publish_rate} Hz'
        )

    def timer_callback(self):
        msg = String()
        msg.data = f"{self.message_prefix}: {random.randint(1,100)}"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
