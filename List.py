list1 = ["Ramesh","Rakshana","Aaditya","Aruna"]
print(type(list1))

print(list1[0])

# To fetch last value
print(list1[-1])

# To print the range of list
print(list1[1:3])
print(list1[-3:-1])

# For loop
for temp in list1 :
    print(temp)

# If statement
if "Ramesh" in list1:
    print("Found")
elif "Rakshana" in list1:
    print("Found")
else:
    print("Not found")
