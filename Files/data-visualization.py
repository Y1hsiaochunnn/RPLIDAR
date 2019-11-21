from rplidar import RPLidar
from math import sin, cos, radians
from matplotlib import pyplot as plt
from time import time

PORT_NAME = "COM3" #/dev/ttyUSB0
TIME_LIMIT = time() + 10

x_coordinates = []
y_coordinates = []

lidar = RPLidar(PORT_NAME)
lidar.connect()

for scan in lidar.iter_measurments():
    angle = round(scan[2], 2)
    distance = round(scan[3] / 10, 2)

    if (distance != 0.0):
        x = round(distance * cos(radians(angle)))
        x_coordinates.append(x)
        y = round(distance * sin(radians(angle)))
        y_coordinates.append(y)

    if (time() >= TIME_LIMIT):
        break

lidar.disconnect()

plt.scatter(x_coordinates, y_coordinates, s = 1 , marker = 'o', c = 'g')
plt.show()