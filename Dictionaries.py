purse=dict()
purse['p1']=768
purse['p2']=768


print(purse)
print(type(purse))

for key in purse:
    print(key,"  ",purse[key])

for key,value in purse:
    print(key,"    ",value)

stuff = dict()
print(stuff.get('candy',-1))