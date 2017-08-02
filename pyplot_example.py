'''
Simple plot using pyplot
'''
import matplotlib.pyplot as plt

def creat_graph():
    x_num = [1, 2, 3]
    y_num = [2, 4, 6]

    plt.plot(x_num, y_num)
    plt.show()

if __name__ == '__main__':
    create_graph()
