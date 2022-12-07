#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
def fact(n):
    if n == 1:
       return 1
    return fact(n - 1) * n
def fact_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# fact(500),
if __name__ == '__main__':
    print(fact(5))
#    print(fact_iter(5))
#    print(fact(5))
#    print(fact_iter(5))
    timing = []
    start = time.time()
    for test_value in range(500):
        fact(test_value)
        end = time.time()
        timing.append(end - start)
        start = end
