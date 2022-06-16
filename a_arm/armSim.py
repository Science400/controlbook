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

ref = signalGenerator.sawtoothWave(frequency=1)

# t = np.linspace(0, 1)
t = np.arange(P.t_start, P.t_end, P.Ts)
y = ref(t)

# fig = plt.figure()
fig, axData = plt.subplots()
axData.set_xlim(P.t_start, P.t_end)
axData.set_ylim(-1.5, 1.5)
line, = axData.plot(t[0], y[0])

def animate(n):
    line.set_data(t[:n], y[:n])
    return line,

anim = animation.FuncAnimation(fig, animate, frames=len(t), interval=P.Ts, blit = True)
plt.show()