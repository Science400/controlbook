import matplotlib.pyplot as plt
import numpy as np
import armParam as P

class armAnimation: 
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots() # Initialize a figure and axis object

        self.handle = [] # Initialize a list object that will be used to contain handles to the patches and line objects.

        self.length = P.length
        self.width  = P.width
        self.theta0 = P.theta0

        X = [0, self.length*np.cos(self.theta0)]  # X data points
        Y = [0, self.length*np.sin(self.theta0)]  # Y data points

        self.ax.axis([-1.5*self.length, 1.5*self.length, -1.5*self.length, 1.5*self.length]) # Set the X and Y axis limits
        self.ax.set_aspect('equal')

        self.ax.plot(X, Y, 'k--') # Plot base line
        armLine, =self.ax.plot(X, Y, lw=5, c='blue')
        self.handle.append(armLine)
        plt.show()

    def update(self, u):
        theta = u[0]
        print(theta)
        X = [0, self.length*np.cos(theta)]  # X data points
        Y = [0, self.length*np.sin(theta)]  # Y data points
        self.handle[0].set_xdata(X)
        self.handle[0].set_ydata(Y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
