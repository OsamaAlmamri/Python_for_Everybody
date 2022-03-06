import re

# https://docs.python.org/3/howto/regex.html

line="osama mohammed ahmed almamari";

print(re.search('mohammed',line))
print(line.find("mohammed"))


print(re.search("^osama",line))
print(line.startswith("osama"))

line2="X-oih89y98y:"
# search if string start with X and has after it zero or more one chars then ':'
print(re.search("^X.*:",line))
print(re.search("^X.*:",line2))
line3="X-oih89y98y:"
line4="X-oih89y98 y:"

# \s   =>not has whiteSpace
# search if string start with X- and has after it not have any wihte Space  then ':'
print(re.search("^X-\S+:",line2))
print(re.search("^X-\S+:",line3))
print(re.search("^X-\S+:",line4))


l5="huih5 7 ho5ih  5fg"

print(re.findall('[0-9]+',l5))
#['5', '7', '5', '5']

print(re.search('[0-9]+',l5))
# True Or False

l7="From: Yemen in Sana\'a :City"

#Greedy Search to find long possible word
print(re.findall('^F.+:',l7))
#["From: Yemen in Sana'a :"]

#Non Greedy Search to find long possible word  will use ?
print(re.findall('^F.+?:',l7))
#['From:']

l8="my email is osama@gmail.com and another email is yemencoder@gmail.com and yhis not email u @gmail.com"

print(re.findall('\S+@\S+',l8))

l9="From Osama@gmail.com"

# '(' and ')' deter mine from where most by match
print(re.findall('^From.\S+@\S+',l9))
print(re.findall('^From.(\S+@\S+)',l9))
# '^' not in the nxt char
print(re.findall('@([^ ]*)',l9))



l9="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"


print(re.findall('@\S+',l9))
print(re.findall('@(\S+)',l9))


x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)




