import matplotlib.pyplot as plt
import numpy as np
# Given points
O = np.array([-53/12, 5/12])
A = np.array([1, -1])
B = np.array([-3, -5])
C = np.array([-4, 6])
# Circle parameters
center = O
radius = np.linalg.norm(A - O)
#To create a circle
theta = np.linspace(0, 2*np.pi, 100)
x_circle = center[0] + radius * np.cos(theta)
y_circle = center[1] + radius * np.sin(theta)
#To create lines
x_line_AB = [A[0], B[0]]
y_line_AB = [A[1], B[1]]
x_line_AC = [A[0], C[0]]
y_line_AC = [A[1], C[1]]
x_line_OB = [O[0], B[0]]
y_line_OB = [O[1], B[1]]
x_line_OC = [O[0], C[0]]
y_line_OC = [O[1], C[1]]
# For plotting graph
plt.figure(figsize=(8, 8))
plt.plot(x_circle, y_circle, label='Circle')
plt.plot(x_line_AB, y_line_AB, label='AB')
plt.plot(x_line_AC, y_line_AC, label='AC')
plt.plot(x_line_OB, y_line_OB, label='OB')
plt.plot(x_line_OC, y_line_OC, label='OC')
#To mark points
plt.scatter([A[0], B[0], C[0], O[0]], [A[1], B[1], C[1], O[1]], color='red')
plt.text(A[0], A[1], 'A', fontsize=12, verticalalignment='bottom')
plt.text(B[0], B[1], 'B', fontsize=12, verticalalignment='bottom')
plt.text(C[0], C[1], 'C', fontsize=12, verticalalignment='bottom')
plt.text(O[0], O[1], 'O', fontsize=12, verticalalignment='bottom')

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid()
plt.legend()
plt.title('Circle with Lines')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.savefig("plot.png")
