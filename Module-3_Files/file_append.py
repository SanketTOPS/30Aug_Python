fl=open('stdata.txt','a')

#fl.write("ID=2\n")
#fl.write("Name:Mitesh\n")

stid=input("Enter ID:")
stnm=input("Enter Name:")

fl.write(f"ID:{stid}\n")
fl.write(f"Name:{stnm}\n")