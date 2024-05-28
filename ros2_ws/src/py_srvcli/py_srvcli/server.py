import rclpy
from rclpy.node import Node

from tutorial_interfaces.srv import AddThreeInts

class MinimalService(Node):

    def __init__(self):
        super().__init__("minimal_server")
        self.server = self.create_service(AddThreeInts, "adder", self.callback)

    def callback(self, req, res):
        res.sum = req.a + req.b + req.c
        self.get_logger().info('Req: a - %d, b - %d, c - %d' % (req.a, req.b, req.c))
        return res

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
