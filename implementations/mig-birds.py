#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    typeArr = [0] * 5
    for i in ar:
        typeArr[i - 1] += 1
    maxVal = 0
    index = 0
    for i in range(0, len(typeArr)):
        if(maxVal < typeArr[i]):
            maxVal = typeArr[i]
            index = i
    return index + 1      

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
