#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:59:33 2020

@author: emeliadaro
"""

import math
import numpy as np
import matplotlib.pyplot as plt

#path ="/Users/emeliadaro/GitHub/project-1-cynthia-and-emmy/Step 3"
#os.chdir(path)
#cwd = os.getcwd()

#print('this is cwd')
#print(cwd)

fin1 = open('length1.txt','r')
fin2 = open('length2.txt','r')
fin3 = open('length3.txt','r')
fin4 = open('length4.txt','r')
fin5 = open('length5.txt','r')
#print(fin1)

#def array(fin):
#    array=[]
#    for row in fin:
#        row=row.rstrip('\n')
##        .strip("()")
#        array.append(row)
#        row.split('()')
##        for index in array:
##            np.split(array,index)
#    print(array)

tupleLength1 =[]
for ln in fin1:
    tupleLength1 = np.append(tupleLength1,fin1.readline())

tupleLength2= []
for ln in fin2:
    tupleLength2 = np.append(tupleLength2,fin2.readline())
    
tupleLength3= []
for ln in fin3:
    tupleLength3 = np.append(tupleLength3,fin3.readline())
    
tupleLength4 = []
for ln in fin4:
    tupleLength4 = np.append(tupleLength4,fin4.readline())
    
tupleLength5 =[]
for ln in fin5:
    tupleLength5 = np.append(tupleLength5,fin5.readline())
#print(tupleLength1)
intarray=[]
for i in range(len(tupleLength1)):
    listElement=list(tupleLength1[i])
    intarray.append(listElement)
print(intarray)
#timearray=tupleLength1[:,0]
#print(timearray)


    
