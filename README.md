# Double_Pendulum_Python

Simulating double pendulum in python using Euler-Lagrange method

![double_pendulum](https://raw.githubusercontent.com/Poscid0n/Double_Pendulum_Python/refs/heads/main/double_pendulum.gif)

---

## Project Overview

This project simulates the motion of a **double pendulum** using the **Euler-Lagrange method**. The double pendulum is a classic example of **deterministic chaos**, where small differences in initial conditions can lead to vastly different outcomes.
### Physics Used
1. Lagrangian Mechanics
2. Explicit Euler Method
### Technologies Used
1. Python (NumPy, Matplotlib)

---

## Installation & Usage

### 1. Install python dependencies
 ```
 pip install numpy matplotlib
```

### 2. Run the simulation
```
python Double_pendulum.py
```

### 3. Customize initial conditions
```
g = 9.8    #value of gravity
m1 , m2 = 1, 2    #mass of the pendulum bobs
r1 , r2 = 0.8 , 0.8    #lengths of the rods
dt = 0.01    #time steps
total_time = 10   #total time the simulation is run for

theta1 = np.deg2rad(90)    #initial angle of the upper rod
theta2 = np.deg2rad(90)    #initial angle for the lower rod
thetadot1 , thetadot2 = 0 , 0    #initial angular velocity of both rods
```

---

## Simulation Preview

![double_pendulum](https://raw.githubusercontent.com/Poscid0n/Double_Pendulum_Python/refs/heads/main/double_pendulum.gif)

---

## How It Works

### 1. Calculate bob's position:
Compute the x, y coordinates of both pendulums based on angles.

### 2. Compute Angular Acceleration:
Use Lagrangian mechanics to derive equations of motion.

### 3. Animate Using Matplotlib:
Generate a frame-by-frame visualization of the pendulum motion.

---

## License

This project is licensed under the **[MIT License](https://github.com/Poscid0n/Double_Pendulum_Python/blob/main/LICENSE)** – feel free to modify and share!

---

## Connect with me

**[LinkedIn](https://www.linkedin.com/in/jain-siddhansh)**
