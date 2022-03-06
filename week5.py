x="sss"
try:
    x=int(x)
except:
    x=-1;
print("x is :", x)


name="osama"
print(name[0:5])
print(name[:3])
print(name[2:])
print(len(name))

print('sam'in name)

name2="  Osama   "
print(name2.lower())
print(name2.upper())
print(dir(name2))

print(name.strip())
print(name.rstrip())
print(name.lstrip())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])