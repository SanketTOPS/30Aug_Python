fl=open('myfile.txt','w')

fl.write("This is Python, This is File")

if fl.writable():
    print("Yes...")
else:
    print("Noo")

