from math import sin, cos, pi
from pylab import *
from lego_robot import *

# This function takes the old (x, y, heading) pose and the motor ticks
# (ticks_left, ticks_right) and returns the new (x, y, heading).


def filter_step(old_pose, motor_ticks, ticks_to_mm, robot_width):
  
    w = robot_width
    l, r = motor_ticks
    l = l * ticks_to_mm
    r = r * ticks_to_mm
    theta = old_pose[2]    # x , y,theta form
    x, y, theta = old_pose
    # Find out if there is a turn at all.
    if (motor_ticks[0] == motor_ticks[1]):
        # No turn. Just drive straight.
        # l, r = motor_ticks
        # l = l * ticks_to_mm
        # r = r * ticks_to_mm
        # theta  = old_pose[2]    # x , y,theta form\
        x = old_pose[0] + l * cos(theta)
        y = old_pose[1] + l * sin(theta)
        # --->>> Implement your code to compute x, y, theta here.
        return (x, y, theta)

    else:


        # Turn. Compute alpha, R, etc.
        alpha = (r - l) / robot_width
        R = l / alpha
        Rw2 = (R + robot_width / 2)
        cx, cy = (old_pose[0] - Rw2 * sin(theta),
                  old_pose[1] - Rw2 * (-cos(theta)))
        theta = (theta + alpha) % (2 * pi)
        x = cx + Rw2 * sin(theta)
        y = cy + Rw2 * (-cos(theta))
        # --->>> Implement your code to compute x, y, theta here.
        return (x, y, theta)

if __name__ == '__main__':
    ticks_to_mm = 0.349
    robot_width = 150.0
    logfile = LegoLogfile()
    logfile.read("robot4_motors.txt")
    pose = (0.0, 0.0, 0.0)   # start with origin

    # Loop over all motor tick records generate filtered position list.
    filtered = []
    for ticks in logfile.motor_ticks:
        pose = filter_step(pose, ticks, ticks_to_mm, robot_width)
        filtered.append(pose)

    # Draw result.
    for pose in filtered:
        print pose
        plot([p[0] for p in filtered], [p[1] for p in filtered], 'bo')
    show()
