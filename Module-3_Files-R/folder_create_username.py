import os


#flnm=input("Enter your folder name:")
#os.mkdir(flnm)


os.chdir("Sanket")
fl=open("sanketdata.txt","a")

sid=input("Enter Sanket's ID:")
ssub=input("Enter Sanket's Subject:")

fl.write(f"ID:{sid}\nSubject:{ssub}\n")