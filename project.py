# DS-542 Winter 2022-2023
# Project 1
# Janmesh Patel
# Tanay Mevada

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


water_value = pd.read_csv(r"C:\Users\jpatel17\Downloads\pydatasets\FirstProject.csv")

y = water_value['Year']
water_consumption = water_value['NYC Consumption(Million gallons per day)'] 
p_c = water_value['Per Capita(Gallons per person per day)']
t_p_c = 0

value1970s = []
value1980s = []
value1990s = []
value2000s = []
value2010s = []
value2020s = []

# Problem 1

# YOUR WORK FOR NUMBER ONE GOES HERE, FIND THE MEAN BY DECADE

for t_y,twater_c in zip(y,water_consumption):
    if t_y>=1970 and t_y<=1979:
        value1970s.append(twater_c)

    if t_y>=1980 and t_y<=1989:
        value1980s.append(twater_c)
    
    if t_y>=1990 and t_y<=1999:
        value1990s.append(twater_c)

    if t_y>=2000 and t_y<=2009:
        value2000s.append(twater_c)    

    if t_y>=2010 and t_y<=2019:
        value2010s.append(twater_c)
    
    if t_y>=2020 and t_y<=2029:
        value2020s.append(twater_c)

print("\n1970s ->",np.mean(value1970s))
print("1980s ->",np.mean(value1980s))
print("1990s ->",np.mean(value1990s))
print("2000s ->",np.mean(value2000s))
print("2010s ->",np.mean(value2010s))
print("2020s ->",np.mean(value2020s))

# Problem 2

# YOUR WORK FOR NUMBER TWO GOES HERE, FIND THE MEDIAN BY DECADE
print("\n1970s ->",np.median(value1970s))
print("1980s ->",np.median(value1980s))
print("1990s ->",np.median(value1990s))
print("2000s ->",np.median(value2000s))
print("2010s ->",np.median(value2010s))
print("2020s ->",np.median(value2020s))

# Problem 3

# YOUR WORK FOR NUMBER THREE GOES HERE, DID PER CAPITA CONSUMPTION INCREASE OR DECREASE EVERY y
for t_y,t_c in zip(y,p_c):
    if  t_y == 1979:
        t_p_c = t_c
        print(t_y,"Current y",t_c)

    elif t_c == t_p_c:
        t_p_c = t_c
        print(t_y,"Water Consumption Per Capita is SAME as Previous y is",t_c)

    elif t_c < t_p_c:
        t_p_c = t_c
        print(t_y,"Water Consumption Per Capita is DECREASE then the Previous y is",t_c)

    elif t_c > t_p_c:
        t_p_c = t_c
        print(t_y,"Water Consumption Per Capita is INCREASE then the Previous y is",t_c)



# Problem 4
# YOUR WORK FOR NUMBER FOUR GOES HERE, FIND THE COST BY DECADE USING YOUR INDIVIDUAL DICTIONARY OF COST PER DECADE







