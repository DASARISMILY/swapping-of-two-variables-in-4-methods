
# first method
'''a=10
b=20
a,b=b,a
print(a)
print(b)'''

#second method
'''a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)'''

#third method
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''

#fourth method[number formattiong] 
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("swaping variables a=%d,b=%d" %(a,b))'''

# for directly giving in run time
'''a=int(input("enter a value"))
b=int(input("enter b value"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''

# for swapping float and string by using number format
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("swapping values are a=%f,b=%f"%(a,b))'''


'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("swapping values are a=.2%f,b=.2%f"%(a,b))'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("swapping values are a=%d,b=%d"%(a,b))'''

#string
a=input("data1")
b=input("data2")
temp=a
a=b
b=temp
print("after swapping a=%s,b=%s"%(a,b))
