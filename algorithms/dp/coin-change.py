#!/bin/python3
import sys
def getWays(n, c):
    # Complete this function
    data = [0] * (n+1)
    data[0] = 1
    for i in c:
        for j in range(1, n + 1):
            if j >= i:
                data[j] += data[j - i]
    print(data[n])
        
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)