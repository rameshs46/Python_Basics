from sklearn.linear_model import  LinearRegression

f = open("Data1.txt","r")
weight = []
numberofpeople = []
for data in f:
    # We will fill the list
    _noofpeople, _weight = data.split(",")
    # print(_noofpeople)
    # print((_weight))
    numberofpeople.append([int(_noofpeople)])
    weight.append(float(_weight))

linearobj = LinearRegression()
# Y = MX + C
linearobj.fit(numberofpeople,weight)
print(linearobj.predict([[10]]))