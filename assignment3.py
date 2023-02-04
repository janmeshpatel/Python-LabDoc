
import math as m 

def ds542(y=1):
    ans = m.sqrt(y)*2
    return ans

print(ds542())




import pandas as pd
import numpy as np


p = pd.read_csv()

print(p.columns)

y = p["Year"]
pop = p["New York City Population"]

for ty,tpop in zip(y,pop):
    print("Year :",ty,", Populatuion :",tpop)