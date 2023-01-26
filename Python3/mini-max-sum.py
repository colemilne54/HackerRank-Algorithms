#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    for i in range(len(arr)):
        currVal = sum(arr) - arr[i]
        if(i == 0):
            min = currVal
            max = currVal
        else:
            if (currVal > max):
              max = currVal
            if (currVal < min):
              min = currVal

    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
