#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    ways = 0
    if n <= m:
        if n == m:
            return 1 if sum(s) == d else 0
        else:
            return 0
    else:
        for i in range(0, n - m + 1):
            val = sum(s[i:i+m])
            if val == d:
                ways += 1
    return ways
        
        

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)