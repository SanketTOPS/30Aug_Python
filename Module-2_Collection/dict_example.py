
from numpy import std


stdata={'id':1,'name':'nirav','sub':'python'}

#print(stdata.get('name'))
#print(stdata['sub'])

"""print(stdata.keys())
print(stdata.values())

if 'nirav' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

#print(len(stdata))

# ------------------------------------- #
print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    print(f"Key={i} and Value={j}")"""

#stdata['id']=2
#stdata['city']='Rajkot'
#stdata.pop('name')
#stdata.clear()
#del stdata['id']
#del stdata
#print(stdata)

newdict=stdata.copy()
print(newdict)