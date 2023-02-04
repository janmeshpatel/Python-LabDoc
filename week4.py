import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\jpatel17\Downloads\pydatasets\week4.csv")


# status = data["STATUS"]
# resolution = data["RESOLUTION_ACTION"]
# for item1,item2 in zip(resolution,status):
#   print("Resolution :" +resolution+",  Status :"+status)

b1 = 0
bb1 = 0
q1= 0
m1 = 0
s1 = 0
c1=0
c2=0


brough = data["BOROUGH"]
resolution = data["RESOLUTION_ACTION"]
status = data["STATUS"]
for b,r in zip(brough,resolution):
    
    if(b=="MANHATTAN"):
        m1 = m1+1
        
    if(b=="QUEENS"):
        q1 = q1+1

    if(b=="BRONX"):
         b1 = b1+1

    if(b=="BROOKLYN"):
        bb1 = bb1+1
    
    if(b=="STATEN ISLAND"):
        s1 = s1+1
            
print("BRONX :",b1 )
print("BROOKLYN :",bb1 )
print("QUEENS :",q1 )
print("MANHATTAN :",m1 )
print("STATEN ISLAND :",s1 )

for b,s in zip(brough,status):
    if(b=="MANHATTAN"):
        if(s=="Closed"):
            c1 = c1+1
    
    if(b=="MANHATTAN"):
        if(s=="Open"):
            c2 = c2+1

print("MANHATTAN, CLOSED : ",c1,",","Percent :",(c1/4520)*100,"%")
print("MANHATTAN, OPEN : ",c2,",","Percent :",(c2/4520)*100,"%")
    



    



    
    