# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
import numpy

x, y, *z = map(int, input().split())

print(numpy.zeros((x, y, *z), dtype=numpy.int32))
print(numpy.ones((x, y, *z), dtype=numpy.int32))
