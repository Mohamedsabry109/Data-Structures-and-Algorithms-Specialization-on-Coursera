# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

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

if __name__ == '__main__':
    input = input();
    n, m = map(int, input.split())
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge(n, m))
