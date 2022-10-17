import rospy, sys
import time
from geometry_msgs.msg import Twist

pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
#rospy.init_node('forward_mode', anonymous=True)
rate = rospy.Rate(10) # 10Hz
move_cmd = Twist()
movementTime = int(seconds)
start = time.time()
flag=True #time flag
# Angular velocity = linear velocity / radius
speed=dropdown_speed # SLOW, NORMAL, FAST
move_cmd.linear.z = 0.00

# CLOCKWISE rotation
if speed =='SLOW':
    move_cmd.linear.y = 0.05
    move_cmd.linear.x = 0.05
elif speed =='NORMAL':
    move_cmd.linear.y = 0.25
    move_cmd.linear.x = 0.25
elif speed == 'FAST':
    move_cmd.linear.y = 0.75
    move_cmd.linear.x = 0.75
while not rospy.is_shutdown() and flag:
    sample_time=time.time()
    if ((sample_time - start) > movementTime):
      flag=False
    pub.publish(move_cmd)
move_cmd = Twist()
pub.publish(move_cmd)
rate.sleep()
