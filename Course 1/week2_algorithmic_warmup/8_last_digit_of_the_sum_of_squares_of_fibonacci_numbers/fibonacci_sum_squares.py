# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

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

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    sum = get_fibonacci_huge(n,10) * get_fibonacci_huge(n+1,10)

    return sum % 10
if __name__ == '__main__':
    n = int(input())
    #print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares(n))