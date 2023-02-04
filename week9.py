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

new_water_data.consumption = new_water_data.consumption * 1000000
print(new_water_data.consumption)



