import os
import numbers

#variables
a = 3
print(a)
print(type(a))

#multiple assignments 
f,g = 10, 20
print(f,g)

a = 4

print(a)

# 1) we can overwrite a variable in same type

a = "hello"
print(a)

# 2) we can overweite a variable in different type


# Mathematical operations
x = 9 
y = 4.1 
z = 0

z = x + y

print(z)

x = z -y
print(x)
print(type(x))

#floating point algebra
print(x*y)
print(x/y)

#break line and continue
ff =4\
    + 3
print(ff)

# powers

print(3**2)
print(9**(1/2))

# maths with string

# overloading
first_word = 'apple'
last_word = 'iphone'
print(first_word + ' ' + last_word)
print(first_word * 2)

#error when substracting and dividng
#print(first_word - last_word)



# pythagorean theorome
''''
a = int(input("Enter length of opposite side"))
b = int(input("Enter length of adjecnt side"))

c = ((a**2)+(b**2))**(1/2)
print(f"The Length of hypotenous is {c}")
'''

print(f"hello {x}")

aList = [1, 2, 3, 4, 5]
print(aList)

strList \
    = ['hi', 'apple']
for j in strList:
    print(j)
xj = 0
for q in aList:
    aList[xj] = aList[xj]*3
    xj += 1

print(aList)
v = 4 not in aList
print(v)

mixedList = aList + strList
print(mixedList)

multiplyList = aList * 3
print(multiplyList)

aList.append(-100)
print(aList)

aList.sort()
print(aList)

xvj = aList.__len__()

print(xvj)

newList = [3, 4, 5, 7, 7, 7, 7, 7, 7, 7, 77 ,7]
print(aList)

print(newList.count(7))

appTup = (1, 2, 3, 4, 5)
print(appTup)

print(type(appTup))

v = list(appTup)

print(type(v))

print(bin(2))

xbf = bool(2 < 3 > 5)
print(xbf)

a = 8 
b = 4

outcome = a == b*2
print(outcome)

# Conjuctive comparison
out0 = 14 > 5 and 7 > 10
out = 14 > 5 or 7 > 10
print(out0)

print(bool('apple'))
app = bool('apple')
print(app)

#Ask the user for the pythagorean triplets, and test whether that is a real triplet

'''
first_side  = int(input("Enter the opposite side length"))
second_side = int(input("Enter the adjacent side length"))
third_side = int(input("Enter the hypotenous side length"))
print("Checking if the 3 sides given are triplets")
check = third_side**(2) == ((first_side**(2)) + ((second_side)**2))

if check == True:
    print("Your given inputs are triplets")
else:
    print("Your given inputs are not triplets")
'''

a = bytes(range(10))

print(a)

mv = memoryview(a)


print(mv)

#Dictionaries
 
    # key/value pair
d = dict()
d['Company'] = 'Apple'
d['revenue'] = [100,200]
print(d)

E = {'genre': 'Blues', 'Band name':'The midnight'}

print(E.values())

# Input two numbers from the user. 
# Create a dictionary with keys 'firstNum', 'SecondNum', 'Product'
'''
del d

d = dict()
num1 = float(input("Enter first number"))
d['firstNum'] = num1
num2 = float(input("Enter Second Number"))
d['SecondNum'] = num2
d['Product'] = num1*num2
print(d.items())
'''

#indexing

arange = range(10, 20)
print(arange)

del aList 

aList = list(arange)
print(aList)

print(aList[-2])

idx = 3
print(aList[idx])

blist = [1, 2, 3, 4, [5, 6, 7], 8, 9]
print(blist[4][1])


#Exercise, get the attribute og penguin 
listlist = [4, 'hi', [5,4,3], 'yo', {'Squirrel':'cute', 'Penguin':'bird'}]

newD = listlist[4]['Penguin']
print(newD)

newV = list(range(5, 11))
print(newV)

print(newV[:4])

print(newV[0:5:2])
print(newV[::-1])

#Use slicing to write "Apple is the best company" from this text

text = 'ynapmoc tseb si elppA'
print(text[::-1][6:14])

print(sum([10,20,30]))

lst = [10,20,30]
listlen  = len(lst)
print(listlen)
print(sum(lst))

# Comute the average of lst

theavg = sum(lst)/len(lst)
print(theavg)