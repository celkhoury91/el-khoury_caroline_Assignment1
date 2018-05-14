#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:23:46 2018

@author: Caroline El Khoury & Andoni Torres
"""


# Question 5 - Calculating the derivative of f(x)

# Analytically, for $\delta =0$, the derivative of f(x) is 1, which is the theoretical value. 

# Importing modules
import numpy as np
import matplotlib.pyplot as plt

x=1
h = np.logspace(-14,-3)

# Define the function
def f(x):
    return x*(x-1)

#Define a function to compute  the derivative   
def derivative(x,h): 
    return (f(x+h)-f(x))/h
    

df = derivative(x,h)

# Plotting the derivative
plt.figure()
plt.plot(h,df, label = 'Numerical')
plt.xlabel('h')
plt.ylabel('dF(x)')
plt.title('Derivative of F(x) Plot')
plt.axhline(y=1, color = 'red', label='Theoretical' ,linestyle= '--')
plt.grid()
plt.legend()
plt.xscale('log')
plt.show()


print('The plot shows deviation from the theoretical value below 10e-11, this can be attributed to numerical uncertainty of floating objects') 