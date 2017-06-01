from pylab import *
from lego_robot import LegoLogfile

logfile = LegoLogfile()
logfile.read("robot4_motors.txt")
plot(logfile.motor_ticks)
show()
'''
1.
f = open("robot4_motors.txt")
left_list = []
right_list = []
for l in f:
    sp = l.split()
    left_list.append(int(sp[2]))
    right_list.append(int(sp[6]))

for i in range(20):
    print left_list[i],right_list[i]
plot(left_list)
plot(right_list)
show()'''
