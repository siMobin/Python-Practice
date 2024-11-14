# 1 arithmetic
v1 = int(input("Enter 1st number"))
v2 = int(input("Enter 2nd number"))
print(v1 + v2)
print(v1 - v2)
print(v1 / v2)
print(v1 * v2)
print(v1 % v2)

# 2 arithmetic Exp-1 too!
v1 = int(input("Enter 1st number"))
v2 = int(input("Enter 2nd number"))
v3 = int(input("Enter 3rd number"))
v4 = int(input("Enter 4th number"))
r1 = v1 - v2
r2 = v3 + v4
print(r1 * r2)  # 4, 3, 2, 5

# 3 arithmetic operation
v1 = 4
v2 = 12
print(v1 + v2)
print(v1 - v2)
print(v1 / v2)
print(v1 * v2)
print(v1 % v2)

# 4 boolean
# x = ""
x = 0
# x = []
# x = True
# x = "Bin"
# x = 23
print(bool(x))

# 5 byteArray
site = "xyz.com"
arr1 = bytearray(site, "utf-8")
arr2 = bytearray(site, "utf-16")
m_view = memoryview(arr1)
print(list(m_view[0:]))
print(arr1)
print(arr2)

size = 4
arr = bytearray(4)
print(arr)

# 6 bytes
site = "xyz.com"
byte = bytes(site, "utf-16")
print(byte)

n = 3
byte = bytes(n)
print(byte)

byte = bytes()
print(byte)

lst = [1, 2, 3]
byte = bytes(lst)
print(byte)

# 7 cont str int
v1 = 100
v2 = "Age"
print(v2 + str(v1))


# 8 Default argument
def full_name(fnam, lname=" Bin"):
    print(fnam + lname)


full_name("Shakib", " Mobin")


def add(a, b, c=4):
    print(int(a) + int(b) + int(c))


add(3, 5, 43)

# 9 Dictionary
dict = {"name": "Shakib", "age": 32, "Course": "Bangladesh Study"}
print(dict["age"])
print(type(dict))

# 10 Explicit
v1 = "32"
print(type(v1))
v2 = int(v1) + 8
print(v2)

v3 = 33.1
print(type(v3))
v4 = int(v3)
print(type(v4))
print(v4)

# 11 for loop
for i in range(1, 10):  # 0 to 9
    print(i)

name = "Shakibul Islam Mobin"
for x in name:
    print(x)

list = [3, 1, 54, 5.23, 51]
for x in list:
    print(x)

for i in range(20, 50):
    print(i)

# 12 loop problem
for i in range(50, 0, -1):
    if i % 2 != 0:
        print(i)


# 13 function
def test(n, name):
    print("How are you")
    print("Your name is " + name)
    print(n)


num = input("Enter a number")
name = input("Enter your name")
test(num, name)


# 14 function problem 1
# find greatest number
# get 3 num
def find_great(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        largest = n1
        print("largest number is the " + str(largest))
    elif n2 > n1 and n2 > n3:
        largest = n2
        print("largest number is the " + str(largest))
    else:
        print("largest number is the " + str(n3))


n1 = int(input("Enter 1st num"))
n2 = int(input("Enter 2nd num"))
n3 = int(input("Enter 3rd num"))
find_great(n1, n2, n3)


# 15 function prroblem 2
# send to function as parameter
# find table in reverse mode
# get num
def table(num):
    print("Table of number")
    # 4 * 10 = 40
    # 4 * 9  = 36
    # .....
    for i in range(10, 0, -1):
        print(str(num) + " * " + str(i) + " = " + str(num * i))


x = int(input("Enter a number"))
table(x)

# 16 implicit
v1 = 3
print(type(v1))
v1 = v1 + 3.3
print(type(v1))
# print("Bin" + 3234)


# 17 keyword Argument
def show(name, num):
    print("name = " + name)
    print("num = " + str(num))


show(num=4739, name="Bin")

# 18 loop example-1
# get a number
# dispaly table of that num

num = int(input("Enter a number to get table "))  # 4
i = 1
while i <= 20:
    # print(i)
    # 4 * 1 = 4
    # 4 * 2 = 8
    # 4 * 3 = 12
    # print(str(num) +" * "+str(i)+" = "+str(num*i))
    print(str(i) + " * " + str(num) + " = " + str(num * i))
    i += 1

# 19 loop example-2
# starting num
# ending num
# starting <  ending

s_n = int(input("Enter a Starting number"))  # 3
e_n = int(input("Enter a Ending number"))  # 10
if s_n < e_n:
    i = s_n  # 3
    while i <= e_n:  # 10
        print(i)
        i += 1
else:
    print("Starting number should be less than ending number")

# 20 loop example-3
# 1 TO 20, odd , add all the number
# 2O TO 1 , EVEN, add all the number
# odd + even
odd_sum = 0
even_sum = 0
for i in range(1, 21):
    if i % 2 != 0:
        odd_sum += i  # 1 + 3 + 5 + 7 ..... 19
        # print(i)
# print(odd_sum)
# print("2nd loop")
for j in range(20, 0, -1):
    if j % 2 == 0:
        even_sum += j
        # print(j)

print("Total result = " + str(even_sum + odd_sum))
# print(even_sum)

# 21 Nested if-else
num = 4
if num % 2 == 0:
    if num % 3 == 0:
        print("Number is divisible by 3 and 2")
    else:
        print("Number is not divisible by 3")
else:
    print("Number is not divisible by 2")

# 22 Operator
v1 = 3
v2 = 5
print(v1 + v2)  # sum of two variable v1
print(v1 == v2)

# 23 parameter


def test(a):
    print(a)


test(4)


def full_name(f_name, l_name):
    print(f_name + l_name)


full_name("Shakib", " Mobin")
full_name("Shakib", " Mobin")

# 24 Relation Operator
a = 3
b = 10
print(a != b)
print(a >= b)
print(a <= b)

username = "skhfs8894"
print(username == "shfs8894")

# 25 Realtion operato exm-1
n1 = int(input("Enter 1st number"))
n2 = int(input("Enter 2nd number"))

if n1 == n2:
    print("Both are equal")
else:
    print("Not equal")


# 26 Relation operator exm-2
n1 = int(input("Enter 1st number"))  # 30
n2 = int(input("Enter 2nd number"))  # 10

if n1 > n2:
    print(n1)
else:
    print(n2)

# 27 Required Arguments
from audioop import add


def add_num(num1, num2=44):
    print(num1 + num2)


add_num(num2=34)

# 28 set
st = {1, 2, 3, 13, 4, 5, 6}
st1 = {3, 4, 5, 12, 14, 56}
print(st.intersection(st1))
print(st)
print(len(st))
print(min(st))

# 29 type-method
print("How are you!")
# type method
a = 3
print(type(a))
b = 3.4
print(type(b))
c = "Shakibil Islam"
print(type(c))
d = "3.3"  # string
print(type(d))
l = [3, 4, 54, 5, 6, 7]
print(type(l))
t = (3, 4, 54, 5, 6, 7)
print(type(t))

# 30 while loop
i = 10
while i >= 0:
    print(i)
    i -= 1
num = 10
while num < 20:
    print("Python")
    num += 1

# 31 while problem
# # 100 to 1, odd
# 1 to 100 , even

i = 100
while i >= 1:
    if i % 2 != 0:
        print(i)
    i -= 1
print("2nd Loop is started from 1 to 100 only even number")
n = 1
while n <= 100:
    if n % 2 == 0:
        print(n)
    n += 1

# 32 problem and solution

# get a number
# display next and prev

num = int(input("Enter a number to see its next and previous"))  # '4' -> 4
pre_num = num - 1
next_num = num + 1

print("User Entered Nunber = " + str(num))
print("Next Number of " + str(num) + " = " + str(next_num))
print("Previous Number of " + str(num) + " = " + str(pre_num))

# 33 problem and solution 2
# to get 2 number
# square + cube = > display to user
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

square_num = num1 * num1
cube_num = num2 * num2 * num2
addition = square_num + cube_num

print("User Entered Number num1 = " + str(num1))
print("User Entered Number num2 = " + str(num2))
print("Square of " + str(num1) + " = " + str(square_num))
print("Cube of " + str(num2) + " = " + str(cube_num))
print(
    "Adittion of "
    + str(square_num)
    + " and "
    + str(cube_num)
    + " is = "
    + str(addition)
)

# 34 problem and solution 3
# get a char
# check, it is vowel or not
# 'a', 'e', 'i', 'o' and 'u'.
char = input("Enter a character")
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print("It is vowel")
else:
    print("It is not vowel")


# 35 problem and solution 4
# to get six subjects marks
# find total, ave, percentage

subj1 = int(input("Enter subject1 marks"))
subj2 = int(input("Enter subject2 marks"))
subj3 = int(input("Enter subject3 marks"))
subj4 = int(input("Enter subject4 marks"))
subj5 = int(input("Enter subject5 marks"))
subj6 = int(input("Enter subject6 marks"))

total = subj1 + subj2 + subj3 + subj4 + subj5 + subj6
ave = total / 6
percentage = (total * 100) / 600
print("Total makrs = " + str(total))
print("Average = " + str(ave))
print("Percentage = " + str(percentage) + "%")

# 36 problem and solution 5
short_name_week = input("Enter short name of the week")

if short_name_week == "mon" or short_name_week == "Mon":
    print("It is Monday")
elif short_name_week == "tue" or short_name_week == "Tue":
    print("It is Tuesday")
elif short_name_week == "wed" or short_name_week == "Wed":
    print("It is Wednesday")
elif short_name_week == "thu" or short_name_week == "Thu":
    print("It is Thursday")
elif short_name_week == "fri" or short_name_week == "Fri":
    print("It is Friday")
elif short_name_week == "sat" or short_name_week == "Sat":
    print("It is Satureday")
elif short_name_week == "sun" or short_name_week == "Sun":
    print("It is Sunday")
else:
    print("Not match in our cases")
