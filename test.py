from math import *

print "hello"


def thingPlus5(thing):
    print "thing = " + str(thing)
    return thing + 5

num = 2

print thingPlus5(num)
print thingPlus5(10)
print thingPlus5(1123)
print thingPlus5(1)

print sqrt(24)


print 5**2

def add(x,y):
    return x+y

def square(x):
    return x**2

def add10(x):
    return x + 10

print add10(square(add(5,6)))

# n = 0
# while n != 42:
#     n = int(raw_input("Type something: "))
#
#     print n+5

for n in range(0,100):
    print "Hi there, this is loop # " + str(n+1)

