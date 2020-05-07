#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback_laser(msg):
  # 720/5 = 144
  # Converts the 720 readings contained inside the LaserScan msg into five distinct readings (180/5 degrees)
  # regions = [ 
  #   min(msg.ranges[0:143]),
  #   min(msg.ranges[144:287]),
  #   min(msg.ranges[288:431]),
  #   min(msg.ranges[432:575]),
  #   min(msg.ranges[576:713]),
  #   ]

  # modify the above code to change inf value to read maximum range
  # receive a value of range between 0 and 10.
  regions = [ 
    min(min(msg.ranges[0:143]), 10),
    min(min(msg.ranges[144:287]), 10),
    min(min(msg.ranges[288:431]), 10),
    min(min(msg.ranges[432:575]), 10),
    min( min(msg.ranges[576:713]), 10),
    ]

  rospy.loginfo(regions)

def main():
  rospy.init_node('reading_laser')
  sub= rospy.Subscriber("/robot/laser/scan", LaserScan, callback_laser)

  rospy.spin()

if __name__ == '__main__':
  main()