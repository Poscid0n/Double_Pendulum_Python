import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

g = 9.8     #value of gravity
m1 , m2 = 1, 2     #mass of the pendulum bobs
r1 , r2 = 0.8 , 0.8      #lengths of the rods
dt = 0.01       #time steps
total_time = 10     #total time the simulation is run for

theta1 = np.deg2rad(90)     #initial angle of the upper rod
theta2 = np.deg2rad(90)     #initial angle for the lower rod
thetadot1 , thetadot2 = 0 , 0       #initial angular velocity of both rods

steps = int(total_time/dt)

_theta1 = np.zeros(steps)   #arrays to store angle
_theta2 = np.zeros(steps)

def bob_position(_theta1, _theta2):
    """Takes angle from an array and returns position of bobs of the pendulum"""
    x1 = r1 * np.sin(_theta1)
    y1 = -r1 * np.cos(_theta1)

    x2 = x1 + r2 * np.sin(_theta2)
    y2 = y1 - r2 * np.cos(_theta2)

    return x1, y1, x2, y2


def acceleration_cal(theta1, theta2, thetadot1, thetadot2):
    """Takes angle and angular velocity and returns angular acceleration"""
    a = -(m1 + m2) * g * np.sin(theta1) * r1 - m2 * r1 * r2 * np.sin(theta1 - theta2) * thetadot2**2
    b = (m1 + m2) * r1**2
    c = m2 * r1 * r2 * np.cos(theta1 - theta2)

    f = -m2 * g * np.sin(theta2) * r2 + m2 * r1 * r2 * thetadot1**2 * np.sin(theta1 - theta2)
    k = m2 * r2**2
    w = m2 * r1 * r2 * np.cos(theta1 - theta2)

    thetaddot2 = (f - a * w / b) / (k - c * w / b)
    thetaddot1 = a / b - c * thetaddot2 / b

    return thetaddot1, thetaddot2


for i in range(1, steps):
    thetaddot1, thetaddot2 = acceleration_cal(theta1, theta2, thetadot1, thetadot2)

    thetadot1 += thetaddot1 * dt
    thetadot2 += thetaddot2 * dt

    theta1 += thetadot1 * dt
    theta2 += thetadot2 * dt

    _theta1[i] = theta1
    _theta2[i] = theta2

x1, y1, x2, y2 = bob_position(_theta1, _theta2)


fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5, 1.5)

line, = ax.plot([], [], 'o-', lw=2)
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def update(frame):
    line.set_data([0, x1[frame], x2[frame]], [0, y1[frame], y2[frame]])
    time_text.set_text(f'Time: {frame * dt:.1f}s')
    return line, time_text

ani = anm.FuncAnimation(fig, update, frames=steps, init_func=init, blit=True, interval=dt*1000)


plt.show()