import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MinimalSubsriber(Node):

    def __init__(self):
        super().__init__("minimal_subscriber")
        self.subscription = self.create_subscription(String, 'chatter', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_subsriber = MinimalSubsriber()

    rclpy.spin(minimal_subsriber)

    minimal_subsriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
