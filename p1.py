# Project Euler - Problem 1 solution
# Solved by: r4ddek (Leonardo F.)

# Problem: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Task: Find the sum of all the multiples of 3 or 5 below 1000.

### Solution Ideas ###
#

### Answer ###
233168

### Code ###
from functools import reduce

result = lambda limit: sum([m for m in range (limit) if m%3==0 or m%5==0])
print(result(1000))

## Or ##
result = lambda limit: reduce(lambda x,y: x+y, [m for m in range (limit) if m%3==0 or m%5==0])
print(result(10))