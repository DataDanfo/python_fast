# -*- coding: utf-8 -*-
"""python_fast_2024_day_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lFoR-MQ8sWjAYNdwhQ7jvJJxhK0z-0Gx

# FOR

1. a = "Apple"
2. a = "Mango"
3. a =  "Guava"
"""

peoples = ["Eric", "Bose", "Holand"]



for op in peoples:
    print(op)

fruits = ["Apple","Mango", "Guava"]

for k in fruits:
  print(k)

numx = [1,2,3]



s = 0
for num in numx:
    s = s + num

print(s)

numbers = [1,2,3,4,5,6,7,8,9,10]

s = 0
for number in numbers:
    s = s + number

print(s)

s = 0 +  1
    s = 1  + 2
    s = 3  + 3
    s = 6

# This program reports how much individuals should pay for their order at
# dinner.
#
# Usage:
#
# $ python bill_splitting.py [name]
#
# For instance:
#
# $ python bill_splitting.py Tom
# Tom should pay 38.55
#
# or:
#
# $ python bill_splitting.py Tim
# Tim did not have dinner



print('There are {} items on the bill'.format(len(bill_items)))


# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that it additionally reports a breakdown of what each
#   person had to eat.
# * Change the program so that if it is called without arguments, a table of
#   how much everybody should pay is displayed

bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramasu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramasu', 4.90],
]

x = [1,45,66,12]

# +
# -
# /
# >
# <
# =
# ==

maxv = -1
for h in x:
    if h > maxv:
        maxv = h
print(maxv)

x = 55
if x == 5:
    print("yes")
else:
    print("No")

s = 0
for t in bill_items:
    if t[0]=="Tom":
        s = s + t[2]

t = ['Tom', 'Calamari', 6.00]
t=  ['Tom', 'American Hot', 11.50]
t =   ['Tom', 'Chocolate Fudge Cake', 4.45]

s1[2]+ s2[2]+s3[2]













k = [[1,2], [1,4], 1, "Love it", [1,4]]

k[0]

k[1]

k[2]

k[3]

k[4]

l = [1,1,1,1]

k[2]