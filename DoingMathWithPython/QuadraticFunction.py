'''
Exploring a Quadatic Function Visually
'''

from matplotlib import pyplot as plt
import math
#defines lists for my points
xVals = []
yVals = []

#draws the graph of the function
def draw_graph(xVals, yVals):
    plt.plot(xVals, yVals)
    plt.show()

#solves the function  for various x values
def calY(xVals):
    for x in xVals:
        y = (x**2) + (2*x) + 1
        yVals.append(y)

if __name__ == '__main__':
    #creates a veriable used for incraminting the while loop
    i = 0
    z = -25
    #while loop to store values to the list xVals
    while i < 50:
        xVals.append(z)
        z += 1
        i += 1
    #pass xVals to the function calY
    calY(xVals)
    #pass xVals and yVals to the function draw_graph
    draw_graph(xVals, yVals)
