'''
Graph of the temp throughout the day
'''

from matplotlib import pyplot as plt

#Draw the graph
def draw_graph(x, y):
    plt.plot(x, y, marker = 'x')
    plt.xlabel('Time of the day in hours')
    plt.ylabel('Tempeture (F)')
    plt.title('Temp throughout the day')
    plt.show()

if __name__ == '__main__':
    y = [32,37,45,46,45,43,37,32]
    x = [0,1,2,3,4,5,6,7,8]
    draw_graph(x, y)
