# data Type
a = 3
print(type(a))
b = 3.4
print(type(b))
c = "siMobin"
print(type(c))
c = 3 + 43j
print(type(c))
l = [3, 4, 54, 5, 6, 7]
print(type(l))
t = (3, 4, 54, 5, 6, 7)
print(type(t))


# tuple
tpl = (2, 3, 4, 5, 6, "siMobin", 2.3)
print(type(tpl))
print(tpl[-3])
# tpl[0] = 10   # 'tuple' object does not support item assignment
# tuple is the immutable, int, float, bool, string
print(tpl)


# String sequence!
print("String is the sequence type of data")
name = "Shakibul Islam"
print(name[4], "\n")

for i in name:
    print(i)


# Set
st0 = {1, 2, 3, 13, 4, 5, 6}
st1 = {3, 4, 5, 12, 14, 56}
print(f"Length: {len(st0)}, Min: {min(st0)}, Max: {max(st0)}")
print(st0.intersection(st1))
print(st0.union(st1))  # Join!


# Range
print("Range Function")
for i in range(1, 20, 2):
    print(i)
print(type(range(3, 20, 1)))


# Conversion -> implicit and explicit
v1 = 3
print(type(v1))
v1 = v1 + 3.3
print(type(v1))

v3 = 33.1
print(type(v3))
v4 = int(v3)
print(type(v4))
print(v4)


# Escape Sequence
print("Hello \nWorld")
print("Hello \t\tWorld")
print("Hello\b\bWorld")
print("Hello \\\\ World")
print("Hello 'World' ")
print("Fuck", end=" You\n\n")


# Dictionary
dict = {"name": "siMobin", "age": 23, "Course": "Python"}
print(dict["age"])
print(type(dict))


# Bytes
lst = [1, 2, 3]
byte = bytes(lst)
print(byte)


# Memoryview
site = "JafriCode.com"
arr1 = bytearray(site, "utf-8")
arr2 = bytearray(site, "utf-16")
m_view = memoryview(arr1)
print(list(m_view[0:]))
print(arr1)
print(arr2)

size = 4
arr = bytearray(4)
print(arr)


# Boolean
x = 0
y = 1
print(f"x is {bool(x)} and y is {bool(y)}")
