#!/usr/bin/env python3

# -*- coding: utf-8 -*-

#EMMY DARO AND CYNTHIA JELKE
#DESCRIPTION: This code is a simulation of a simple pendulum that graphs its 
#             position, velocity, and acceleration vs. time and also calculates
#             its period
#HOURS TO COMPLETE: 8 hours


import numpy as np

import matplotlib.pyplot as plt 



###########################################################
#initialize
#ARGUMENTS: 
#           a = the index of the pendulum lengths used in the simulation (an 
#               integer 0-4)
#           b = the starting angle of the pendulum
#DESCRIPTION: initializes the length and values studied in the simulation 
#             (position, velocity, and acceleration)
#OUTPUT:
#           postheta = the angle that the pendulum starts at
#           veltheta = the starting velocity (0)
#           acctheta = the starting acceleration (0)
#           length = the length of the pendulum in meters

def initialize(a,b): 

    length = lengths[a]

    postheta = b

    veltheta = 0

    acctheta = 0

    return postheta, veltheta, acctheta, length 


###########################################################
#update
#ARGUMENTS:
#           pos = the position of the pendulum at that moment
#           vel = the velocity of the pendulum at that moment
#           acc = the acceleration of the pendulum at that moment
#           length = the length of the pendulum being used
#DESCRIPTION: finds the following value for position, velocity, and 
#             acceleration)
#OUTPUT:
#           posNext = the new position of the pendulum
#           velNext = the new velocity of the pendulum
#           accNext = the new acceleration of the pendulum
    
def update(pos,vel,acc,length):

    dt = (10/10000) #time step

    posNext = pos+vel*dt #eulers method to find position

    velNext = vel+acc*dt #eulers method to find velocity

    accNext = (-9.81*np.sin(pos*np.pi/180)/length) #eulers method to find acceleration 

    return posNext, velNext, accNext


###########################################################
#plot
#ARGUMENTS:
#           posNext = the position of the pendulum at that moment
#           velNext = the velocity of the pendulum at that moment
#           accNext = the acceleration of the pendulum at that moment
#           length = the length of the pendulum being used
#DESCRIPTION: calculates and prints the period of the pendulum and plots
#             position vs. time, velocity vs. time, and accceleration vs. 
#             time

def plot(posNext,velNext,accNext,length):
    
    #initializes arrays with one index and a value of 0
    posx = np.zeros((1,1)) 

    velx = np.zeros((1,1))

    accx = np.zeros((1,1))

    t = np.zeros((1,1))
    

    i = 0

    #builds three arrays that contain the position, velocity and acceleration
    #values of the pendulum at each time stamp
    while i < len(time): 

        #finds the position, velocity, and acceleration of the pendulum at the 
        #next time stamp
        temp = update(posNext, velNext, accNext, length) 

        posNext = temp[0] 

        velNext = temp[1] 

        accNext = temp[2]
        
        #adds the new values to the arrays created at the beginning of the 
        #function
        posx = np.append(posx,length*np.sin(posNext*np.pi/180)) 

        velx = np.append(velx,length*velNext*np.cos(posNext*np.pi/180))

        accx = np.append(accx,length*(-np.sin(posNext*np.pi/180)*(velNext**2)+np.cos(posNext*np.pi/180)*accNext)) 

        t = np.append(t,time[i])

        i += 1 

    prev = 0

    #finds and calculates the period of the pendulum
    for i in range(0,len(posx)-1): 

        if(posx[i]<0 and posx[i+1]>0): 

            period = time[i] - prev

            prev = time[i]

    print("The period of the pendulum is " + str(round(period, 4)) + " seconds!") 

            
    #plots the position vs. time graph
    plt.xlabel("time (s)")

    plt.ylabel("X position (m)")

    plt.title("Pendulum Length " + str(length) + " Position vs. Time")

    plt.plot(t,posx) 

    plt.show()

    
    #plots the velocity vs. time graph
    plt.xlabel("Time (s)")

    plt.ylabel("X velocity (m/s)")

    plt.title("Pendulum Length " + str(length) + " Velocity vs. Time")

    plt.plot(t,velx)

    plt.show()

   
    #plots the acceleration vs. time graph
    plt.xlabel("Time (s)")

    plt.ylabel("X acceleration (m/s/s)")

    plt.title("Pendulum Length " + str(length) + " Acceleration vs. Time")

    plt.plot(t,accx) 

    plt.show()
    
##########################################################################
###MAIN###
##########################################################################
    
#an array of the lengths of our pendulums in meters
lengths=np.array([.34,.43,.53,.62,.72])

#setting the times checked with an increment of 1/1000
time = np.linspace(0,10,10000)

#Finding and Graphing for 6o degrees
print("The starting angle is 60 degrees")

for i in range(5):
    #set which pendulum length you're using
    a = i
    #set initial angle
    b= np.pi/3
    
    #initialize the needed variables
    pos, vel, acc, length = initialize(a,b)
    
    #plots position vs. time, velocity vs. time, and acceleration vs. time as well
    #as calculates the period 
    plot(pos, vel, acc, length)

#Finding and Graphing for 120 degrees
print("The starting angle is 120 degrees")
    
for i in range(5):
    #set which pendulum length you're using
    a = i
    #set initial angle
    b= 2*np.pi/3
    
    #initialize the needed variables
    pos, vel, acc, length = initialize(a,b)
    
    #plots position vs. time, velocity vs. time, and acceleration vs. time as well
    #as calculates the period 
    plot(pos, vel, acc, length)

