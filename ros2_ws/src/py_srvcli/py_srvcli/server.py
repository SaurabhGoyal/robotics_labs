import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class MinimalService(Node):

    def __init__(self):
        super().__init__("minimal_server")
        self.server = self.create_service(AddTwoInts, "adder", self.callback)

    def callback(self, req, res):
        res.sum = req.a + req.b
        self.get_logger().info('Req: a - %d, b - %d' % (req.a, req.b))
        return res

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
