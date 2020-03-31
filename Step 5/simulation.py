#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:17:36 2020

@author: emeliadaro
"""

import numpy as np
import matplotlib.pyplot as plt 

lengths=np.array([.34,.43,.53,.62,.72])
time = np.linspace(0,10,10000)


def initialize(a,b): 
    length = lengths[a]
    postheta = np.pi/b
    veltheta = 0
    acctheta = 0
    return postheta, veltheta, acctheta, length 

def update(pos,vel,acc,length):
    dt = (10/10000) 
    posNext = pos+vel*dt #eulers method to find position
    velNext = vel+acc*dt #eulers method to find velocity
    accNext = -9.81*np.sin(pos)/length #eulers method to find acceleration 
    return posNext, velNext, accNext, length


def plot(posNext,velNext,accNext,length)
    posx = np.zeros((1,1)) 
    velx = np.zeros((1,1))
    accx = np.zeros((1,1))
    t = np.zeros((1,1))
    i = 0
    while i < len(time): 
        temp = update(posNext, velNext, accNext, length) 
        posNext = temp[0] 
        velNext = temp[1] 
        accNext = temp[2]
        posx = np.append(posx,length*np.sin(posNext)) 
        velx = np.append(velx,length*velNext*np.cos(posNext))
        accx = np.append(accx,length*(-np.sin(posNext)*(velNext**2)+np.cos(posNext)*accNext)) 
        t = np.append(t,time[i])
        i += 1 
    prev = 0
    for i in range(0,len(posx)-1): 
        if(posx[i]<0 and posx[i+1]>0): 
            period = time[i] - prev
            prev = time[i]
    print("Pendulum period " + str(period)) 
            
    plt.xlabel("time (s)")
    plt.ylabel("X position (m)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,posx) 
    plt.show()
    
    plt.xlabel("Time (s)")
    plt.ylabel("X velocity (m/s)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,velx)
    plt.show()
   
    plt.xlabel("Time (s)")
    plt.ylabel("X acceleration (m/s/s)")
    plt.title("Pendulum Length " + str(length))
    plt.plot(t,accx) 
    plt.show()

'''so to make these functions work heres my call idea that im too fried to try:
    call initialize with the given pendulum lenth and arbitrary theta
        that will return position as the starting angle and velocity/acceleration at 0
then push those values into plot which will update them and append each updated value
into an array that then gets plotted with each cycle of the loop in plot 