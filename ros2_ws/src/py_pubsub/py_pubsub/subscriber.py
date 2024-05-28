import rclpy
from rclpy.node import Node

from tutorial_interfaces.msg import Num

class MinimalSubsriber(Node):

    def __init__(self):
        super().__init__("minimal_subscriber")
        self.subscription = self.create_subscription(Num, 'chatter', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.num)

def main(args=None):
    rclpy.init(args=args)

    minimal_subsriber = MinimalSubsriber()

    rclpy.spin(minimal_subsriber)

    minimal_subsriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
