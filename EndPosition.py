# End Position of 3/4 DOF Manipulator using Python.

import math
def matrix_multiplication(m_a, m_b):
       if len(m_a[0]) != len(m_b):
        return None
       else:
        m_c = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    m_c[i][j] += m_a[i][k] * m_b[k][j]
        return m_c

def calculate_matrix(alpha, theta, d, a):
    alpha = math.radians(alpha)
    theta = math.radians(theta)
    mat1 = [[math.cos(theta1), (-1)*math.sin(theta1)*math.cos(alpha1), math.sin(theta1)*math.cos(alpha1), (a1)*math.cos(theta1)], 
    [math.sin(theta1), math.cos(theta1)*math.cos(alpha), (-1)*math.cos(theta1)*math.sin(alpha1),(a1)*math.sin(theta1)], 
    [0, math.sin(alpha1), math.cos(alpha1), d1], 
    [0, 0, 0, 1]]
    
    mat2 = [[math.cos(theta2), (-1)*math.sin(theta2)*math.cos(alpha2), math.sin(theta2)*math.cos(alpha2), (a2)*math.cos(theta2)], 
    [math.sin(theta2), math.cos(theta2)*math.cos(alpha2), (-1)*math.cos(theta2)*math.sin(alpha2),(a2)*math.sin(theta2)], 
    [0, math.sin(alpha2), math.cos(alpha2), d2], 
    [0, 0, 0, 1]]
    
    mat3 = [[math.cos(theta3), (-1)*math.sin(theta3)*math.cos(alpha3), math.sin(theta3)*math.cos(alpha3), (alpha3)*math.cos(theta3)], 
    [math.sin(theta3), math.cos(theta3)*math.cos(alpha3), (-1)*math.cos(theta3)*math.sin(alpha3),(a3)*math.sin(theta3)], 
    [0, math.sin(alpha3), math.cos(alpha3), d3], 
    [0, 0, 0, 1]]
    
    return matrix_multiplication(mat1, matrix_multiplication(mat2, mat3))

theta1 = math.degrees(int(input("Enter the value of theta1: ")))
theta2 = math.degrees(int(input('Enter the value of theta2: ')))
theta3 = math.degrees(int(input('Enter the value of theta3: ')))
a1 = int(input('Enter the value of a1: '))
a2 = int(input('Enter the value of a2: '))
a3 = int(input('Enter the value of a3: '))
d1 = int(input('Enter the value of d1: '))
d2 = int(input('Enter the value of d2: '))
d3 = int(input('Enter the value of d3: '))
alpha1 = math.degrees(90)
alpha2 = math.degrees(-90)
alpha3 = math.degrees(0)
t1 = calculate_matrix(alpha1, theta1, d1, a1)
t2 = calculate_matrix(alpha2, theta2, d2, a2)
t3 = calculate_matrix(alpha3, theta3, d3, a3)
t = matrix_multiplication(t1, matrix_multiplication(t2, t3))
print("Transformation matrix:")
print(t)
print("The positional value p_x: ", round(t[0][3], 2))
print("The positional value p_y: ", round(t[1][3], 2))
print("The positional value p_z: ", round(t[2][3], 2))

