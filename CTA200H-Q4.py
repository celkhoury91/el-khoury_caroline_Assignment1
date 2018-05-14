#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:14:19 2018

Authors: Caroline El Khoury & Andoni Torres

"""
# Question 4

#This program runs the iterative function z_{i+1} = z_i^2 + c on where z_0 = c 
#and c = x + iy. After each iteration, the color map shows how much the function
#augmented.

# Importing modules
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

iterations = 10  #Set number of iterations 

data = np.linspace(-2,2,100) # x and y domain

array_data = [[] for m in range(iterations-1)] 
for i in range(len(array_data)):
    array_data[i] = [[]for m in range(100)]

for x in data:  # Row loop
    list_data = []
    for y in data: # Column loop
        # This part initializes the paramters
        ite = 0 # Iteration steps initialized at 0
        c = complex(x,y) # x: real, y:imaginary
        z = 0 + c # First element of function
        list_z = []
        list_pow = []
        # This part runs the iterative function
        while ite < iterations:
            ite = ite + 1
            z = pow(z, 2) + c
            lenght_z = abs(z.real)
            list_z.append(lenght_z)
        # This part stores the powers to which the function augmened
        for i in range(iterations-1):
            strenght = np.ceil(np.log10(list_z[i+1]/list_z[0]))
            list_pow.append(strenght)
        list_data.append(list_pow)
    for j in array_data:
        for k in range(len(j)):
            j[k].append(list_data[k][array_data.index(j)])
            
# Plotting the iterations
for ite in array_data:
    fig, ax = plt.subplots()
       
    cax = ax.imshow(ite, interpolation='nearest', cmap=cm.gist_gray)
    ax.set_title('Deviation after iteration '+str(array_data.index(ite)+1))      
    
    cbar = fig.colorbar(cax, ticks=[0,5,10,20, 50, 100, 250], label = 'Growth ($10^\n$)')
    cbar.ax.set_yticklabels(['0','5', '10', '20', '50', '100', '250'])  
    plt.xlabel('Real axis from -2 to 2')
    plt.ylabel('Imaginary axis from -2 to 2')
    plt.show()