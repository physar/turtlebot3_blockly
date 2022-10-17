import rospy, sys
import time
from geometry_msgs.msg import Twist

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
#rospy.init_node('stop_node', anonymous=True)
rate = rospy.Rate(10) # 10Hz
move_cmd = Twist()
start = time.time()
flag=True #time flag

move_cmd.linear.z = 0.00
move_cmd.linear.y = 0.00
move_cmd.linear.x = 0.00

while not rospy.is_shutdown() and flag:
    sample_time=time.time()
    if ((sample_time - start) > 2):
      flag=False
    pub.publish(move_cmd)
move_cmd = Twist()
pub.publish(move_cmd)
rate.sleep()
