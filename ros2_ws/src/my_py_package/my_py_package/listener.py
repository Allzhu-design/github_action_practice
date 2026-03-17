import rclpy
from rclpy.node import Node
from std_msgs.msg import String

"""ROS2 Listener node."""


class Listener(Node):
    """A simple ROS2 node that listens to messages."""

    def __init__(self):
        """Initialize the listener node."""
        super().__init__('listener')
        self.declare_parameter('topic', 'chatter')
        topic = self.get_parameter('topic').get_parameter_value().string_value

        self.subscription = self.create_subscription(String, topic, self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info(f'Listener started, listening to {topic!r}')

    def listener_callback(self, msg):
        """Process received messages."""
        self.get_logger().info(f'I heard: {msg.data!r}')


def main(args=None):
    """Run the listener node."""
    rclpy.init(args=args)
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
