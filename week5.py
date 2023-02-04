import pandas as pd
import numpy as np

film_data = pd.read_csv(r"C:\Users\jpatel17\Downloads\pydatasets\week5.csv")



print(film_data['Country'][0])
counter = 0
for row in film_data['Country']:
    if( row != "United States of America"):
        counter += 1
print(counter)

m_count = 0

si_count = 0 

bk_count = 0

bx_count = 0

q_count = 0

for row in film_data['Borough']:
    if( row == "Manhattan"):
        m_count+= 1
    elif( row == "Brooklyn"):
        bk_count+= 1
    elif (row == "Bronx"):
        bx_count+= 1
    elif (row == "Staten Island"):  
        si_count+= 1
    elif (row == "Queens"):
        q_count+= 1
    else:
        pass

print("Manhattan: " + str(m_count))

print("Brooklyn: " + str(bk_count))

print("Bronx: " + str(bx_count))

print("Staten Island: " + str(si_count))

print("Queens: " + str(q_count))

tv_count = 0
for row in film_data['Category']:
    if(row == 'Television'):
        print(row)