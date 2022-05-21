# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:03:29 2019

@author: Nick
"""
import numpy as np
import matplotlib.pyplot as plt

# Constants
eps0 = 8.854e-12
k = 1/(4*np.pi*eps0)

# Variables
a = 1
d = 2*a
b = a**3/d
q1 = 1
q2 = -q1*a/d

# Grid of y, z points
L=5*a
ny, nz = 1000, 1000
y = np.linspace(-L, L, ny)
z = np.linspace(-L, L, nz)
Y, Z = np.meshgrid(y,z)

# Electric Field
Ey = k*(q1*(-d+Y)*((-d+Y)**2+Z**2)**(-3/2) - q2*(b-Y)*((b-Y)**2+Z**2)**(-3/2))
Ez = k*(q1*Z*((-d+Y)**2+Z**2)**(-3/2) + q2*Z*((b-Y)**2+Z**2)**(-3/2))

# Create circle for surface of sphere
theta = np.linspace(0,2*np.pi,1000)
y1 = a*np.cos(theta)
z1 = a*np.sin(theta)

# Plot E-field
plt.figure(figsize = (8,8))
plt.streamplot(y, z, Ey, Ez, linewidth=1, density=3, arrowstyle='->', arrowsize=1.5);
plt.plot(y1,z1)
plt.xlabel('y [m]')
plt.ylabel('z [m]')
plt.title('E-field')
plt.legend(['Surface of conductor','E-field lines'])
plt.grid()

# Calculate Ez along z-axis
Ez1 = k*(q1*z*((-d)**2+z**2)**(-3/2) + q2*z*((b)**2+z**2)**(-3/2))

# Plot Ez
plt.figure(figsize = (8,8))
plt.plot(z,Ez1)
plt.xlabel('z [m]')
plt.ylabel('Ez [V/m]')
plt.title('Ez along the z-axis')
plt.grid()

# Calculate surface charge
sigma = eps0*k*(q1*(a-d*np.cos(theta))*(a**2+d**2-2*a*d*np.cos(theta))**(-3/2)
            + q2*(a-b*np.cos(theta))*(a**2+b**2-2*a*b*np.cos(theta))**(-3/2))

# Plot surface charge
plt.figure(figsize = (8,8))
plt.plot(theta,sigma)
plt.xlabel('theta [rad]')
plt.ylabel('surface charge density [C/m/m]')
plt.title('Induced surface charge density of the conductor')
plt.grid()