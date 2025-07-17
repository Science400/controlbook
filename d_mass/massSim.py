import sys
sys.path.append('./lib')
from matplotlib import animation
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
import massParam as P
import signalGenerator

refz = signalGenerator.sineWave(frequency=1/2, amplitude=np.pi, yoffset=0)

t = np.arange(P.t_start, P.t_end, P.Ts)
z = refz(t)

# fig = plt.figure()
fig, axs = plt.subplots(2, 1)
axData = axs[0]
axMass = axs[1]
zLine, = axData.plot([], [], color="tab:orange")
massPatch = axMass.add_patch(Rectangle((0, 0), P.width, P.height))

def animateInit():
    axData.set_xlim(P.t_start, P.t_end)
    axData.set_ylim(np.min(z)*1.2, np.max(z)*1.2)
    zLine.set_data(t[0], z[0])
    axData.legend(['$z$'])

    axMass.set_aspect('equal')
    axMass.set_xlim(np.min(z)-P.width/2*1.2, np.max(z)+P.width/2*1.2)
    axMass.set_ylim(np.min(z)-P.width/2*1.2, np.max(z)+P.width/2*1.2)
    massPatch.set(xy=(P.z0-P.width/2, 0), width=P.width, height=P.height, color='tab:orange')

    return zLine, massPatch

def animate(n):
    zLine.set_data(t[:n], z[:n])
    massPatch.set(xy=(z[n]-P.width/2, 0), width=P.width, height=P.height)
    return zLine, massPatch

anim = animation.FuncAnimation(fig, animate, frames=len(t), init_func=animateInit, interval=P.Ts*1000, blit=True)
plt.show()

