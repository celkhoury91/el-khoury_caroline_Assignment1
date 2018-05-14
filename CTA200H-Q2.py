#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 09:37:14 2018

@author: Caroline El Khoury & Andoni Torres
"""

# Question 2: 

# Importing Modules
import numpy as np
import matplotlib.pyplot as plt

#a

# Recursive Factorial function
def factorial(n):
    if n ==0:
        return 1
    else: 
        return n*factorial(n-1)

# Binominal Coefficient function for a given n and k
def coeficients(n,k):
    result = int(factorial(n)/(factorial(k)*factorial(n-k)))
    return result


#b Print the first 20 coefficients to Pascal's Triangle
    
print("The first 20 lines of Pascal's triangle are:")

for i in range(19):
    line= [] #line in Pascals' triangle
    for j in range(0,i+1):
        line.append(coeficients(i,j))
    print(line)


#c
    
# Define a function to calculate the probability of getting k heads and n roll with a bias of p
def probability(n,p,k):
    result = coeficients(n,k)*p**k*(1-p)**(n-k)
    return result

# Calling the function and setting the parameters
prob1 = probability(4, 0.25, 1)
print("The probability of the baseball player to obtain at least one hit is %s " %prob1)
    
#d Simulating the experiment N times with skew p 

# Setting the parameters
N = [10,50,100]
skew = [0.15, 0.25, 0.5, 0.75]

# Simulating for N times with skew p
for i in N:	
    y=np.arange(1, i+1)
    x = [[] for x in range(len(skew))]
    for k in range(len(skew)):
        for j in range(i):
            t1= probability(i,skew[k],j)
            x[k].append(t1)
            
	# plotting the figures for each N       
    plt.figure()
    plt.xlabel('Events')
    plt.ylabel('Probability')
    plt.title('Simulated experiment for N=%s' %i)
    plt.plot(y,x[0],'o-', label="p=0.15")
    plt.plot(y,x[1],'o-', label="p=0.25")
    plt.plot(y,x[2],'o-', label="p=0.5" )
    plt.plot(y,x[3],'o-', label="p=0.75")
    plt.legend()
    plt.grid()
    plt.show()


