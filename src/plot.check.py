import numpy as np
import matplotlib.pyplot as plt
import random
if __name__ == '__main__':
    x=[1,2,3,4,5,6,7,8] #id nodes
    y=[1,2,3,4,5,6,7,8]
    x2=[12,13,14,15,16,17,18]
    y2=[12,13,14,15,16,17,18]
    plt.plot(x,y,'o',color='blue',ms=5)
    x1,y1=x,y
    plt.arrow(1,1,2,2,width=0.05)
    plt.arrow(3,3,-2,-2,width=0.05)

    plt.show()