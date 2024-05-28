import sys
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class MinimalClient(Node):

    def __init__(self):
        super().__init__("minimal_client")
        self.client = self.create_client(AddTwoInts, "adder")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waiting for service ...')

    def send(self, a, b):
        req = AddTwoInts.Request()
        req.a, req.b = a, b
        self.future = self.client.call_async(req)
        self.get_logger().info('Req: a - %d, b - %d' % (req.a, req.b))
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info('Response for %d + %d : %d' % (a, b, self.future.result().sum))

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClient()
    minimal_client.send(int(sys.argv[1]), int(sys.argv[2]))

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
