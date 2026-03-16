import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.declare_parameter("topic", "chatter")
        topic = self.get_parameter("topic").get_parameter_value().string_value

        self.subscription = self.create_subscription(
            String, topic, self.listener_callback, 10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info(f'Listener started, listening to "{topic}"')

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
