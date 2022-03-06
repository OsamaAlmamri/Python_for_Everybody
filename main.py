print('hello world')

x=10
while x>0:
    print(x)

    x=x-1

print(int(97.6))
name=input("enter file name")

hamdel =open(name,'r')
counts =dict()

for line in hamdel:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

print(counts)



