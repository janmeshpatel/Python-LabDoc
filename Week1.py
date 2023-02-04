sq = pd.read_csv(r"C:\Users\jpatel17\Downloads\pydataset\squirrel.csv")
print(sq.columns)
print(sq['X'])
print(sq['X'].tolist())
xlist = sq['X'].tolist()
print(xlist[0])

s = {1,2,3}
print(s)

s.add(4)
print(s)

s.update([5,6])
print(s)

s.remove(6)
print(s)


t = (1,2,3)
print(t)

tx = tuple(xlist)
print(tx)

sy = set(xlist)
print(sy)

dis = {"name" : "janmesh","month" : 12, 123 : "123"}
print(dis)
print(dis["month"])
dis["year"]= 2022
print(dis)