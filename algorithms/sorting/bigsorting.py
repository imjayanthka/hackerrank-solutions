#!/bin/python3

import sys

def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    
def bigSorting(arr):
    # Complete this function
    n = len(arr)
    quickSort(arr, 0, n - 1)
    return arr

if __name__ == "__main__":
    # n = int(input().strip())
    arr = [31415926535897932384626433832795,1,3,10,3,5]
    # arr_i = 0
    # for arr_i in range(n):
    #    arr_t = str(input().strip())
    #    arr.append(arr_t)
    result = bigSorting(arr)
    print ("\n".join(map(str, result)))