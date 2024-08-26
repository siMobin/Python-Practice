# https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true
import numpy

x = input().split()
# numpy.set_printoptions(legacy="1.13")
print(numpy.eye(int(x[0]), int(x[1]), k=0))
