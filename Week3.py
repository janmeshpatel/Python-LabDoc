import pandas as pd
import numpy as np




def columns_to_list(csv_file_name, column_name):
    sq = pd.read_csv(csv_file_name)
    column = sq[column_name]
    column_list = column.tolist()
    return(column_list)
    
def column_type(column_list):
    print(type(column_list[1]))


    
sq2 = columns_to_list(r"C:\Users\jpatel17\Downloads\pydataset\squirrel.csv","Eating")
column_type(sq2)

clm = "Running"

s_column = columns_to_list(r"C:\Users\jpatel17\Downloads\pydataset\squirrel.csv",clm)
print(s_column)

def percent_true(boolean_list):
    boolean_sum = sum(boolean_list)
    list_length = len(boolean_list)
    percent = boolean_sum / list_length

    return percent

print("The percentage "+ clm +" in the census is :")
print(percent_true(s_column)*100)








