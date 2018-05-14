#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:10:52 2018

@author: caroline.elkhoury
"""
# Question 3


# Importing modules
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import signal, ndimage
import scipy.special as sco
import matplotlib.image as mpimg
from astropy.convolution import AiryDisk2DKernel
from astropy.convolution import convolve

#a

x = np.linspace(0,10, num = 1000)

# Bessel function
def bessel(m,x):
    return integrate.quad(integrand, 0, np.pi, args=(m,x))[0] 

# Integrand function
def integrand(theta,m,x):
    return (1/np.pi)*np.cos(m*theta - x*np.sin(theta))
# Plotting the Bessel function for a changing x values for a given m
'''
plt.figure()

for m in range(5):
    res = np.zeros(x.size)
    for i in range(x.size):
        res[i] = bessel(m,x[i])  
    plt.plot(x,res, label = 'm = %d'%(m))
    
plt.grid()
plt.legend()
plt.xlim(0,10)
#plt.show()
'''
#b
 
# Define a function for the intensity seen in the focal plane

# Define the constants

lam = 0.5 # wavelength 
a = 23 # radius of the telescope
R = 18 # distance from the aperture to the focal plane
I0 = 1000 # intensity from the centre

# Define the point spread function
def pointspread(x): 
    return I0*(2*bessel(1,x)/x)**2


# Define an empty array for q
q = np.zeros([10, 10])

for i in range(q.shape[0]):
    for j in range(q.shape[1]):
        pos_x = i - q.shape[0]/2
        pos_y = j - q.shape[1]/2
        q[i,j] = np.sqrt(pos_x**2+pos_y**2)
q /= q.shape[0]
print(q)

'''
plt.figure()
plt.imshow(q)
#plt.show()
'''      
x = (2*np.pi*a*q)/(lam*R)  

psf = np.zeros_like(x)
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        psf[i,j] = pointspread(x[i,j])
'''
plt.figure()
plt.imshow(np.log10(psf),cmap = 'gray')
plt.colorbar(label = 'Log10 of Intensity (arb)')
plt.title('Point-Spread Function')
plt.xlabel('x (meters)')
plt.ylabel('y (meters)')
plt.savefig("q3b.pdf")
plt.show()
'''
# c
# Load the image
img = mpimg.imread('galaxy.png')
img = img.mean(axis=-1)

# Plot the Original Image
plt.figure()
plt.imshow(img)
plt.title("Original")
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()

    
conv_matrix = AiryDisk2DKernel(10) # from astropy package
conv_img = signal.convolve2d(img, conv_matrix)

# Plot convolve image
plt.figure()
plt.imshow(conv_img)
plt.title("Convolved Image")
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()
        
