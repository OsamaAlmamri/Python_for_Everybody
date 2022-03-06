students=list()

students.append("osama")
students.append("ali")

print(type(students))
print("osama" in (students))
print("osama" not in (students))

print(len(students))
print(max(students))
print(min(students))
print(students.sort())


num=[1,4,7,3,8,3,11]
num.sort()
print(num)
print(sum(num))
print(len(num))
print(sum(num)/len(num))


days="Saturday,Sunday,Monday,Tuesday,Thursday,Wednesday"

arr_day=days.split(',')
print(arr_day)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

t = [9, 41, 12, 3, 74, 15]

print(t[2:4])

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])



fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for w in words:
        if w not in lst:
            lst.append(w)

print(lst)
