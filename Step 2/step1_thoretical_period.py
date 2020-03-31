#EMMY DARO & CYNTHIA JELKE
#THEPRETICAL PERIOD CALCULATION AND PLOT
#PROJECT 1 PART 3


import math
import numpy as np
import matplotlib.pyplot as plt

length_list=[34,43,53,62,72]
length_array=np.array(length_list)
print(length_list)

#function: calculate_period takes an array of pendulum legnths as an input and 
#returns an array of corresponding periods
def calculate_period(length_array):
    periods=[]
    length_list=list(length_array)
    for i in length_list:
        p=(2*math.pi*(i/9.81)**(1/2))
        p=round(p,2)
        periods.append(p)
    periods_array=np.array(periods)
    return periods_array

periods_array = calculate_period(length_list)
print(periods_array)

fig=plt.plot(length_array,periods_array,'o', color='black')
plt.ylabel('period in seconds')
plt.xlabel('length in cm')
plt.title('Period time as a function of pendulum length')
        
#This model calculates the theoretical legnth of a pendulum based off of of an 
#equation. There will be inevitable discrepancies between the calculated data 
#and the data we collect experimentally. The formula calculation does not take
#into account forces due to friction and air resistence that will slow the 
#pendulum down and alter its behavior. 