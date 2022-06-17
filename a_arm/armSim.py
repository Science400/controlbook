import sys
from matplotlib import animation
sys.path.append('./lib')
import matplotlib.pyplot as plt
import numpy as np
import armParam as P
from armAnimation import armAnimation
import signalGenerator

# animation = armAnimation()
# animation.update([np.pi/2, 0])

ref = signalGenerator.sineWave(frequency=1/5, amplitude=np.pi, yoffset=np.pi)

# t = np.linspace(0, 1)
t = np.arange(P.t_start, P.t_end, P.Ts)
y = ref(t)

# fig = plt.figure()
fig, axs = plt.subplots(2, 1)
axData = axs[0]
axArm = axs[1]
dataLine, = axData.plot([], [])
armLine, = axArm.plot([], [])

def animateInit():
    axData.set_xlim(P.t_start, P.t_end)
    axData.set_ylim(np.min(y)*1.2, np.max(y)*1.2)
    dataLine.set_data(t[0], y[0])

    axArm.set_aspect('equal')
    axArm.set_xlim(-P.length*1.2, P.length*1.2)
    axArm.set_ylim(-P.length*1.2, P.length*1.2)
    axArm.plot([0,P.length], [0,0], linestyle='dashed', color='black')
    armLine.set_data([0,P.length*np.cos(P.theta0)], [0,P.length*np.sin(P.theta0)])
    armLine.set_linewidth(5)
    armLine.set_color('orange')

    return dataLine, armLine

def animate(n):
    dataLine.set_data(t[:n], y[:n])
    armLine.set_data([0,P.length*np.cos(y[n])], [0,P.length*np.sin(y[n])])
    return dataLine, armLine

anim = animation.FuncAnimation(fig, animate, frames=len(t), init_func=animateInit, interval=P.Ts*1000, blit=True)
plt.show()