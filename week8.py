import numpy as np
import pandas as pd

file_path = r"C:\Users\jpatel17\Downloads\pydatasets\Dog_Bite.csv"
bite_dataset = pd.read_csv(file_path)
brooklyn_bites = bite_dataset.reset_index(names = 'old_index')
print(brooklyn_bites.old_index[3333])

