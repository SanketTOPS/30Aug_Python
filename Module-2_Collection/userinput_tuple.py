mytup=[]

n=int(input("Enter number of elements:"))

for i in range(n):
    el=input("Enter your element:")
    mytup.append(el)

print(tuple(mytup))