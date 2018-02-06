#!/bin/python3

import sys
import re
def camelcase(s):
    # Complete this function
    pattern = re.compile('[A-Z]')
    return(len(list(pattern.findall(s))) + 1)

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)