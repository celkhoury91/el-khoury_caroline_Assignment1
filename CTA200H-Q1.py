#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:30:23 2018

@author: Caroline El Khoury & Andoni Torres
"""
# Question 1: A script thqt finds and replaces a given word in all the .txt files in the working directory. 

import os

find = input("find: ")
replace = input("replace: ")

if not os.path.exists("replace"):
    os.makedirs("replace")

for file in os.listdir("."):
    if file.endswith(".txt"):
        with open(file, "rt") as file_in:
            with open("replace/"+str(file), "wt") as file_out:
                for line in file_in: 
                    file_out.write(line.replace(str(find), str(replace)))
                    if str(find) in file_in:
                        file_out.write(line.replace(str(find), str(replace)))
                    else: 
                        print('No instances found')
                        


