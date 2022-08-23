import sys
sys.path.append('./lib')
from matplotlib import animation
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
import pendulumParam as P
import signalGenerator

ref = signalGenerator.sineWave(frequency=1/5, amplitude=np.pi, yoffset=np.pi)
refTheta = signalGenerator.sineWave(frequency=1/5, amplitude=np.pi/4, yoffset=np.pi/2)

t = np.arange(P.t_start, P.t_end, P.Ts)
z = ref(t)
theta = refTheta(t)

# fig = plt.figure()
fig, axs = plt.subplots(2, 1)
axData = axs[0]
axPendulum = axs[1]
zLine, = axData.plot([], [])
thetaLine, = axData.plot([], [])
cartPatch = axPendulum.add_patch(Rectangle((P.z0-P.w/2, P.gap), P.w, P.h))
rodLine, = axPendulum.plot([], [])

def animateInit():
    axData.set_xlim(P.t_start, P.t_end)
    axData.set_ylim(np.min(z)*1.2, np.max(z)*1.2)
    zLine.set_data(t[0], z[0])
    thetaLine.set_data(t[0], z[0])

    axPendulum.set_aspect('equal')
    axPendulum.set_xlim(np.min(z)-P.w/2, np.max(z)+P.w/2)
    axPendulum.set_ylim(0, (P.h+P.ell)*1.2)
    cartPatch.set(xy=(P.z0-P.w/2, P.gap), width=P.w, height=P.h)
    cartPatch.set(color='orange')
    rodLine.set_data([z[0], z[0]+P.ell*np.sin(theta[0])], [P.gap+P.h, -(P.gap+P.h+P.ell*np.cos(theta[0]))])

    return zLine, thetaLine, cartPatch, rodLine

def animate(n):
    zLine.set_data(t[:n], z[:n])
    thetaLine.set_data(t[:n], theta[:n])
    # armLine.set_data([0,P.length*np.cos(y[n])], [0,P.length*np.sin(y[n])])
    cartPatch.set_x(z[n]-P.w/2)
    rodLine.set_data([z[n], z[n]+P.ell*np.cos(theta[n])], [P.gap+P.h, P.gap+P.h+P.ell*np.sin(theta[n])])
    return zLine, thetaLine, cartPatch, rodLine

anim = animation.FuncAnimation(fig, animate, frames=len(t), init_func=animateInit, interval=P.Ts*1000, blit=True)
plt.show()