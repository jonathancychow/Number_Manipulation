import numpy as np
from itertools import *

def pentagonal_numbers (n):
    # pentagonal_numbers = np.array(1)
    pentagonal_numbers=[]
    for i in range(1, n):
        pentagonal_numbers = np.append(pentagonal_numbers,i*(3*i-1)/2)
    return pentagonal_numbers

numbers = pentagonal_numbers(3000)
combination = combinations (numbers,2)

b=(0,0)
for k in combination:
    if k[0]+k[1] in numbers and k[1]-k[0] in numbers:
        np.vstack([b, k])


b