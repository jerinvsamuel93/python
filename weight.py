Weight=input("enter the weight")
print(type(Weight))
Weight=int(Weight)
print(type(Weight))
Lkg= input("k or p")
print(Lkg)
if(Lkg == 'k'):
    w = Weight/0.45
    print(w)
    print("your weight is {} pound".format(w))
elif (Lkg == 'p'):
    w= Weight*0.45
    print("your weight is {} kg".format(w))

else:
    print("Please enter either l or p ")