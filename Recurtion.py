#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
def fact(n):
    if n < 0:
      raise ValueError
    if n == 0:
       return 1
    return fact(n - 1) * n
def fact_iter(n):
    if n < 0:
        raise ValueError
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def fact_tail(n, acc=1):
    if n < 0:
        raise ValueError
    if n == 0:
     return acc
    return fact_tail(n - 1, acc*n)

if __name__ == '__main__':
    print(fact(5))
#    print(fact_iter(5))
#    print(fact(5))
#    print(fact_iter(5))
    timing = []
    start = time.time()
    for test_value in range(5000):
        fact(test_value)
    end = time.time()
    timing.append(end - start)
    start = end
    for test_value in range(5000):
        fact_iter(test_value)
    end = time.time()
    timing.append(end - start)
    start = end
    print(timing)