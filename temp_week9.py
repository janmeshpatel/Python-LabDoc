import pandas as pd
from matplotlib import pyplot as plt

dataset_url = 'https://data.cityofnewyork.us/api/views/ia2d-e54m/rows.csv'

water_data = pd.read_csv(dataset_url)
print(water_data.columns)

new_water_data = water_data.rename(columns = {'NYC Consumption(Million gallons per day)': 'consumption',
                                              'New York City Population': 'population',
                                              'Per Capita(Gallons per person per day)': 'per_capita',
                                              'Year': 'year'})
print(new_water_data.columns)

new_water_data.consumption = new_water_data.consumption * new_water_data.per_capita

print(water_data.to_csv('new_water_data.csv'))
    
print(len(water_data.to_csv()))
########################
'''
Time to do some graphing... just leave this code as is.
If your code aboe is correct, this should work with no changes
'''
#######################


# Create a MatPlotLib Pyplot with two lines on one graph
fig, ax1 = plt.subplots(figsize=(10, 8))
ax2 = ax1.twinx() # Create a second graph with a twin x axis, in our case this is the year

ax1.plot(new_water_data.year, new_water_data.consumption)
ax2.plot(new_water_data.year, new_water_data.per_capita)

ax1.set_xlabel("Year", fontsize = 14)
ax1.set_ylabel("Total Consumption in Gallons", fontsize=14)
ax1.tick_params(axis="y")

ax2.set_ylabel("Per Capita Consumption in Gallons", fontsize=14)
ax2.tick_params(axis="y")

fig.suptitle("NYC Water: Total Consumption vs Per Capita Consumption", fontsize=24)

plt.show()
