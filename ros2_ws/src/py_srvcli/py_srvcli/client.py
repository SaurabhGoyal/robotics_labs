import sys
import rclpy
from rclpy.node import Node

from tutorial_interfaces.srv import AddThreeInts

class MinimalClient(Node):

    def __init__(self):
        super().__init__("minimal_client")
        self.client = self.create_client(AddThreeInts, "adder")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waiting for service ...')

    def send(self, a, b, c):
        req = AddThreeInts.Request()
        req.a, req.b, req.c = a, b, c
        self.future = self.client.call_async(req)
        self.get_logger().info('Req: a - %d, b - %d, c - %d' % (req.a, req.b, req.c))
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info('Response for %d + %d + %d : %d' % (a, b, c, self.future.result().sum))

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClient()
    minimal_client.send(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
