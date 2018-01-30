#!/bin/python3

import sys

def maxSubarray(arr):
    # Complete this function
    max_subSeq = max_subArray = max_current = arr[0]
    mis = [x for x in arr]
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] >= arr[j] and mis[i] < mis[j] + arr[i] and arr[i] > 0:
                mis[i] = mis[j] + arr[i]
        max_current = max(max_current + arr[i], arr[i])
        if max_subArray < max_current:
            max_subArray = max_current
    return[max_subArray, max(mis)]
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = maxSubarray(arr)
        print (" ".join(map(str, result)))
