# Uses python3
import sys
from random import randint


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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



def fibnacci_sum(m,n):

    if m > 0:
        last_digit = ((get_fibonacci_huge(n,10) + get_fibonacci_huge(n+1,10)-1)  - (get_fibonacci_huge(m,10) + get_fibonacci_huge(m-1,10)-1) ) %10
    else:
        last_digit = (get_fibonacci_huge(n,10) + get_fibonacci_huge(n+1,10) - 1) % 10

    return last_digit

if __name__ == '__main__':
    input = input();
    from_, to = map(int, input.split())
    #print(fibonacci_partial_sum_naive(from_, to))
    print(fibnacci_sum(from_,to))

    # while(True):

    #     max_value = 1000
    #     a = int(randint(0,max_value))
    #     b = int(randint(0,max_value)+2)
        
    #     if (b > a):

    #         print("a : ", a,"b : ",b)

    #         res1 = fibonacci_partial_sum_naive(a,b)
    #         res2 = fibnacci_sum(a,b)


    #         if (res1 != res2):
                
    #             print("Wrong , ",res1," ",res2)
    #             break
    #         else:
    #             print("OK")