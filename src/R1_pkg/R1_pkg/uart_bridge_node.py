import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class UARTBridgeSubscriber(Node):
	
	def __init__(self):
		super().__init__('uart_bridge')
		self.subscription = self.create_subscription(String,'topic',self.listener_callback,10)
		self.subscription
		
	def listener_callback(self,msg)
		self.get_logger().info('I heard: "%s"' % msg.data)
		
def main(args=None):
	rclpy.init(args=args)
	
	uart_bridge = UARTBridgeSubscriber()
	
	rlcpy.spin(uart_bridge)
	
	uart_bridge.destroy_node()
	rlcpy.shutdown()
	
	
if __name__ == '__main__':
	main()
