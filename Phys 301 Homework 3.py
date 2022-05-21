# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:03:29 2019

@author: Nick
"""
import numpy as np
import matplotlib.pyplot as plt

# Grid of x, y points
L=4
nx, ny = 100, 100
x = np.linspace(-L, L, nx)
y = np.linspace(-L, L, ny)
X, Y = np.meshgrid(x,y)

# Constants
eps0 = 8.854e-12
k = 1/(4*np.pi*eps0)

# Variables
a = 1
b = 2
q = 1

def Ex(qq,aa,bb):
    return k*qq*(X-aa)/((X-aa)**2+(Y-bb)**2)**(3/2)
               
def Ey(qq,aa,bb):
    return k*qq*(Y-bb)/((X-aa)**2+(Y-bb)**2)**(3/2)

Ex = Ex(-q,a,0) + Ex(-q,-a,0) + Ex(3*q,0,b) + Ex(-q,0,-b)  
Ey = Ey(-q,a,0) + Ey(-q,-a,0) + Ey(3*q,0,b) + Ey(-q,0,-b)

# demo of streamplot for a vector field
fig = plt.figure(figsize = (8,8))
plt.streamplot(x, y, Ex, Ey, linewidth=1, density=2, arrowstyle='->', arrowsize=1.5);