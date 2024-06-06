import sys
sys.path.append('./lib')
from matplotlib import animation
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np
import satelliteParam as P
import signalGenerator

refTheta = signalGenerator.sineWave(frequency=1/5, amplitude=np.pi, yoffset=0)
refPhi = signalGenerator.sineWave(frequency=1/5, amplitude=np.pi, yoffset=0, phaseshift=-np.pi/18)

t = np.arange(P.t_start, P.t_end, P.Ts)
theta = refTheta(t)
phi = refPhi(t)

def hexagonVerticesAtAngle(angle, radius):
    return [(np.cos(np.pi/3 * i + angle) * radius, np.sin(np.pi/3 * i + angle) * radius) for i in range(6)]

def lineVerticesAtAngle(angle, length):
    return [(-np.cos(angle) * length/2, -np.sin(angle) * length/2), (np.cos(angle) * length/2, np.sin(angle) * length/2)]

# fig = plt.figure()
fig, axs = plt.subplots(2, 1)
axData = axs[0]
axSatellite = axs[1]
thetaLine, = axData.plot([], [])
phiLine, = axData.plot([], [])
bodyRadius = P.width/2
bodyHexagon = hexagonVerticesAtAngle(P.theta0, bodyRadius)
bodyPatch = axSatellite.add_patch(Polygon(bodyHexagon, closed=True))
bodyCorners = axSatellite.scatter(bodyHexagon[0][0], bodyHexagon[0][1], color='tab:orange')
panelLine, = axSatellite.plot([], [])

def animateInit():
    axData.set_xlim(P.t_start, P.t_end)
    axData.set_ylim(np.min(theta)*1.2, np.max(theta)*1.2)
    thetaLine.set_data(t[0], theta[0])
    thetaLine.set_color('tab:orange')
    phiLine.set_data(t[0], phi[0])
    phiLine.set_color('tab:blue')
    axData.legend(['$\\theta$', '$\\phi$'])

    axSatellite.set_aspect('equal')
    axSatellite.set_xlim(-P.length/2*1.2, P.length/2*1.2)
    axSatellite.set_ylim(-P.length/2*1.2, P.length/2*1.2)
    lineStart, lineEnd = lineVerticesAtAngle(P.phi0, P.length)
    panelLine.set_xdata([lineStart[0], lineEnd[0]])
    panelLine.set_ydata([lineStart[1], lineEnd[1]])
    panelLine.set_color('tab:blue')
    panelLine.set_linewidth(2)
    bodyHexagon = hexagonVerticesAtAngle(theta[0], bodyRadius)
    bodyPatch.set_xy(bodyHexagon)
    bodyPatch.set(color='tab:orange', zorder=3.5)
    bodyCorners.set_offsets([bodyHexagon[0], bodyHexagon[3]])
    bodyCorners.set_zorder(4)

    return thetaLine, phiLine, bodyPatch, panelLine, bodyCorners

def animate(n):
    thetaLine.set_data(t[:n], theta[:n])
    phiLine.set_data(t[:n], phi[:n])
    lineStart, lineEnd = lineVerticesAtAngle(phi[n], P.length)
    panelLine.set_xdata([lineStart[0], lineEnd[0]])
    panelLine.set_ydata([lineStart[1], lineEnd[1]])
    bodyHexagon = hexagonVerticesAtAngle(theta[n], bodyRadius)
    bodyPatch.set_xy(bodyHexagon)
    bodyCorners.set_offsets([bodyHexagon[0], bodyHexagon[3]])
    return thetaLine, phiLine, bodyPatch, panelLine, bodyCorners

anim = animation.FuncAnimation(fig, animate, frames=len(t), init_func=animateInit, interval=P.Ts*1000, blit=True)
plt.show()