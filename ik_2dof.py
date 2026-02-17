

# defining the length of the link


import matplotlib.pyplot as plt
import math
# length of the links
L1 = 8  # length in cm
L2 = 5  # length in cm

# Desired Position of End effector
x = 6
y = 10

# Equations for Inverse kinematics


def inverse_kinematics(x, y, L1, L2):
    r = math.sqrt(x**2 + y**2)
    # Check reachability
    if r > L1 + L2:
        return None
    theta_2 = math.acos((x**2 + y**2-L1**2-L2**2)/(2*L1*L2))
    theta_1 = (math.atan2(y, x)) - \
        (math.atan2((L2*math.sin(theta_2)), (L1 + L2*math.cos(theta_2))))

    return math.degrees(theta_1), math.degrees(theta_2)


# call the function
angles = inverse_kinematics(x, y, L1, L2)

if angles is None:
    print("Target position is unreachable")
else:
    theta_1, theta_2 = angles
    print("Theta 1 (deg):", theta_1)
    print("Theta 2 (deg):", theta_2)

theta_1, theta_2 = angles
A_1 = math.radians(theta_1)
A_2 = math.radians(theta_2)


# forward kinematics
def forward_kinematics(A_1, A_2):
    x1 = L1*math.cos(A_1)
    y1 = L1*math.sin(A_1)

    x2 = x1+L2*math.cos(A_1+A_2)
    y2 = y1+L2*math.sin(A_1+A_2)

    return [0, x1, x2], [0, y1, y2]


x_points, y_points = forward_kinematics(A_1, A_2)


plt.figure(figsize=(6, 6))
plt.plot(x_points, y_points, 'o-', linewidth=4, markersize=10)
plt.plot(x, y, 'r*', markersize=12, label='Target')

plt.xlim(-(L1+L2+1), L1+L2+1)
plt.ylim(-(L1+L2+1), L1+L2+1)
plt.grid(True)
plt.legend()
plt.title(f"2-Link Arm Reaching ({x}, {y})")
plt.show()
plt.show()
