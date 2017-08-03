'''
Enhanced Projectile Trajectory Comparison Program
'''

from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile Motion of a Ball')
    plt.legend(uList)
    plt.show()

def frange(start, final, interval):
    numbers = []
    while start < final:
        number.append(start)
        start = start + interval
    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    #Time of flight
    t_flight = 2*u*math.sin(theta)/g
    #find time intervals
    intervals = frange(0, t_flight, 0.001)
    #list of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x, y)

if __name__ == '__main__':
    uList = []
    i = 0
    try:
        numInputs = int(input('How many trajectories?'))
        while i < numInputs:
            u = float(input('Enter the initial velocity (m/s): '))
            theta = float(input('Enter the angle of projection (degrees): '))
            uList.append(u)
            i += 1
    except ValueError:
        print('You entered an invalid input!')
    else:
        for u in uList:
            draw_trajectory(u, theta)
