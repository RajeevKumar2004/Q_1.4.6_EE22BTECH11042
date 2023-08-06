import numpy as np

A = np.array([1, -1])
B = np.array([-4, 6])
C = np.array([-3, -5])
# O is a point of intersection of perpendicular bisectors of AB and AC
O = np.array([-53 / 12, 5 / 12])

#To find angle BOC
dot_pt_O = (B - O) @ ((C - O).T)
norm_pt_O = np.linalg.norm(B - O) * np.linalg.norm(C - O)
cos_theta_O = dot_pt_O / norm_pt_O
angle_BOC = np.degrees(np.arccos(cos_theta_O))
print("angle BOC = " + str(angle_BOC))

#To find angle BAC
dot_pt_A = (B - A) @ ((C - A).T)
norm_pt_A = np.linalg.norm(B - A) * np.linalg.norm(C - A)
cos_theta_A = dot_pt_A / norm_pt_A
angle_BAC = np.degrees(np.arccos(cos_theta_A))
#To check whether the answer is correct or not
print("angle BAC = " + str(angle_BAC))
if angle_BOC == 2 * angle_BAC:
  print("\nangle BOC = 2 times angle BAC\nHence the give statement is correct")
else:
  print("\nangle BOC ≠ 2 times angle BAC\nHence the given statement is wrong")
