import rclpy 
from rclpy import Node

from std_msg.msg import String

class PlannerNode(Node):

	def __init__(self):
		super().__init__('planner')
		self.publisher_ = self.create_publisher(String, 'topic', 10)
		timer_period = 1
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0
		
	def timer_callback(self):
		msg = String()
		msg.data = 'Hello World: %d' % self.i
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%s"' msg.data)
		self.i +=1
		
def main(args=None):
	rclpy.init(args=args)
	planner = PlannerNode()
	
	rclpy.spin(planner)
	
	planner.destro_node()
	rclpy.shutdown()
	
	
if __name__ == '__main__':
	main()
		
