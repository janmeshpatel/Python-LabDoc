# DS-542 Winter 2022-2023
# Project 1
# Janmesh Patel
# Tanay Mevada

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


water_data = pd.read_csv(r"C:\Users\jpatel17\Downloads\pydatasets\FirstProject.csv")

year = water_data['Year']
water_consumption = water_data['NYC Consumption(Million gallons per day)'] 
per_capita = water_data['Per Capita(Gallons per person per day)']
temp_per_capita = 0

data1970s = []
data1980s = []
data1990s = []
data2000s = []
data2010s = []
data2020s = []

# Problem 1

# YOUR WORK FOR NUMBER ONE GOES HERE, FIND THE MEAN BY DECADE

for tyear,twater_consumption in zip(year,water_consumption):
    if tyear>=1970 and tyear<=1979:
        data1970s.append(twater_consumption)

    if tyear>=1980 and tyear<=1989:
        data1980s.append(twater_consumption)
    
    if tyear>=1990 and tyear<=1999:
        data1990s.append(twater_consumption)

    if tyear>=2000 and tyear<=2009:
        data2000s.append(twater_consumption)    

    if tyear>=2010 and tyear<=2019:
        data2010s.append(twater_consumption)
    
    if tyear>=2020 and tyear<=2029:
        data2020s.append(twater_consumption)

print("\nActual Data by Decades :")
print("1970s Decades :",data1970s)
print("1980s Decades :",data1980s)
print("1990s Decades :",data1990s)
print("2000s Decades :",data2000s)
print("2010s Decades :",data2010s)
print("2020s Decades :",data2020s)
    
print("\nProblem : 1 (Mean Water Consumption by Decades):")
print("1970s ->",np.mean(data1970s))
print("1980s ->",np.mean(data1980s))
print("1990s ->",np.mean(data1990s))
print("2000s ->",np.mean(data2000s))
print("2010s ->",np.mean(data2010s))
print("2020s ->",np.mean(data2020s))

# Problem 2

# YOUR WORK FOR NUMBER TWO GOES HERE, FIND THE MEDIAN BY DECADE
print("\nProblem : 2 (Median Water Consumption by Decades) :")
print("1970s ->",np.median(data1970s))
print("1980s ->",np.median(data1980s))
print("1990s ->",np.median(data1990s))
print("2000s ->",np.median(data2000s))
print("2010s ->",np.median(data2010s))
print("2020s ->",np.median(data2020s))

# Problem 3

# YOUR WORK FOR NUMBER THREE GOES HERE, DID PER CAPITA CONSUMPTION INCREASE OR DECREASE EVERY YEAR
print("\nProblem : 3 (PER CAPITA CONSUMPTION INCREASE OR DECREASE  BY EVERY YEAR):")
for tyear,tper_capita in zip(year,per_capita):
    if  tyear == 1979:
        temp_per_capita = tper_capita
        print(tyear,"Current Year is ",tper_capita)

    elif tper_capita == temp_per_capita:
        temp_per_capita = tper_capita
        print(tyear,"Water Consumption Per Capita is SAME as Previous Year is",tper_capita)

    elif tper_capita < temp_per_capita:
        temp_per_capita = tper_capita
        print(tyear,"Water Consumption Per Capita is DECREASE then the Previous Year is",tper_capita)

    elif tper_capita > temp_per_capita:
        temp_per_capita = tper_capita
        print(tyear,"Water Consumption Per Capita is INCREASE then the Previous Year is",tper_capita)



# Problem 4

# YOUR WORK FOR NUMBER FOUR GOES HERE, FIND THE COST BY DECADE USING YOUR INDIVIDUAL DICTIONARY OF COST PER DECADE
rate = {'1970s': 10.61, '1980s': 4.67, '1990s': 7.41, '2000s': 4.33, '2010s': 8.70, '2020s': 2.74}

sum_1970s = 0
sum_1980s = 0
sum_1990s = 0
sum_2000s = 0
sum_2010s = 0
sum_2020s = 0
for tyear,tper_capita in zip(year,per_capita):
    if tyear>=1970 and tyear<=1979:
        trate = rate['1970s']
        sum_1970s = sum_1970s + (tper_capita * trate)
        

    if tyear>=1980 and tyear<=1989:
        trate = rate['1980s']
        sum_1980s = sum_1980s + (tper_capita * trate)
       
    
    if tyear>=1990 and tyear<=1999:
        trate = rate['1990s']
        sum_1990s = sum_1990s + (tper_capita * trate)
        

    if tyear>=2000 and tyear<=2009:
        trate = rate['2000s']
        sum_2000s = sum_2000s + (tper_capita * trate)
           

    if tyear>=2010 and tyear<=2019:
        trate = rate['2010s']
        sum_2010s = sum_2010s + (tper_capita * trate)
        
    
    if tyear>=2020 and tyear<=2029:
        trate = rate['2020s']
        sum_2020s = sum_2020s + (tper_capita * trate)
        

print("\nProblem : 4 (Cost Per Capita as per Decades):")
print("1970s : $"+str(sum_1970s))
print("1980s : $"+str(sum_1980s))
print("1990s : $"+str(sum_1990s))
print("2000s : $"+str(sum_2000s))
print("2010s : $"+str(sum_2010s))
print("2020s : $"+str(sum_2020s))
# OPTIONAL EXTRA CREDIT

# YOUR WORK FOR THE EXTRA CREDIT GOES HERE, GRAPH THE POPULATION AND THE CONSUMPTION USING PYPLOT
 
plt.plot(water_data['Year'],water_data['New York City Population'],marker = ".", mfc="r")  
plt.xlabel("Year")
plt.ylabel("New York City Population")
plt.show()



plt.plot(water_data['Year'],water_data['NYC Consumption(Million gallons per day)'],marker = ".", mfc="r")  
plt.xlabel("Year")
plt.ylabel("Total Water Consumption")
plt.show()






