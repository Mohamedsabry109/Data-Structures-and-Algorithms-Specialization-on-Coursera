# Uses python3
import sys
from random import randint

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def pisano_period(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
          
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    
    pisano_period_ = pisano_period(m)
    n = n % pisano_period_

    if n == 0:
        return 0

    previous = 0
    current  = 1    
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_sum(n):

    last_digit = (get_fibonacci_huge(n,10) + get_fibonacci_huge(n+1,10) - 1) % 10

    return last_digit

if __name__ == '__main__':
    input = input()
    n = int(input)
    #print(fibonacci_sum_naive(n))
    print(fibonacci_sum(n))
    
    # while(True):

    #     max_value = 10
    #     a = int(randint(0,max_value))
    #     #b = int(randint(0,max_value))
        
    #     print("a : ", a)

    #     res1 = fibonacci_sum_naive(a)
    #     res2 = fibonacci_sum(a)
        
    #     print("a : ", a)

    #     if (res1 != res2):
            
    #         print("Wrong , ",res1," ",res2)
    #         break
    #     else:
    #         print("OK")
