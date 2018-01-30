#!/bin/python3

import sys
def candies(n, arr):
    # Complete this function
    data = [1] * n
    add = 0
    #print(distribution)
    for i in range(1, n):
            if arr[i] > arr[i - 1]:
                data[i] = data[i - 1] + 1
            elif (arr[i - 1] > arr[i]) and (data[i] >= data[i - 1]):
                data[i - 1] = data[i] + 1 
            else:
                data[i] = 1
    for i in range(0, n):
        add = add + data[i]
    return add

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = candies(n, arr)
    print(result)