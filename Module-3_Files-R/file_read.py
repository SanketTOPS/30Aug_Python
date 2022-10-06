fl=open("stdata.txt","r")

#print(fl.read())

#print(fl.readline())

#print(fl.readlines())
#print(fl.readlines()[2])

n=1
for i in fl:
    #print(i)
    print(F"Line:{n} = {i}")
    n+=1