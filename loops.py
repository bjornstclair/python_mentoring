__author__ = 'kburke'


fruits = ["Apple", "Orange", "Grape", "Pineapple"]

print range(len(fruits))

for idx in range(len(fruits)):
    print str(idx+1)+ ": "+ fruits[idx]

for fruit in fruits:
    print fruit

for (idx, fruit) in enumerate(fruits):
    print str(idx+1)+ ": "+ fruits[idx]