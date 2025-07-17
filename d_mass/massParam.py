# Inverted Pendulum Parameter File
import numpy as np
# import control as cnt

# Physical parameters of the arm known to the controller
m =  5   # mass kg
k =  3   # spring constant N/m
b =  0.5 # damping coefficient N-sec/m

# parameters for animation
width = 1.0
height = 1.2

# Initial Conditions
z0 =  0 # initial position of mass, m
zdot0 =  0 # initial velocity of mass m/s

# Simulation Parameters
t_start = 0 # Start time of simulation
t_end =  10 # End time of simulation
Ts =  0.01 # sample time for simulation
t_plot = 0.1 # the plotting and animation is updated at this rate

# dirty derivative parameters
# sigma =  # cutoff freq for dirty derivative
# beta =   # dirty derivative gain

# saturation limits
# F_max =   # Max force, N

