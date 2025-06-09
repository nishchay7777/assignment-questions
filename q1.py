"""The provided code stub reads two integers from STDIN, a and b.
Add code to print three lines where:

The first line contains the sum of the two numbers.

The second line contains the difference of the two numbers (a - b).

The third line contains the product of the two numbers."""


import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(a+b)
print(a-b)
print(a*b)
