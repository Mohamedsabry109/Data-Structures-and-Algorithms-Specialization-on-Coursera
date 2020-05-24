# python3
from random import randint


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_product = 0
    first_max_index = 0
    for first in range(n):
        if (numbers[first_max_index] <= numbers[first]):
            first_max_index = first

    while (True):
        second_max_index = randint(0,n-1)
        if second_max_index != first_max_index:
            break

    for second in range(n):
        if (numbers[second_max_index] <= numbers[second] and second != first_max_index):

            second_max_index = second

    max_product = numbers[first_max_index] * numbers[second_max_index]

    return max_product

if __name__ == '__main__':

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
    


# STRESS TEST TEMPLATE
"""
    while(True):

        max_number_of_elements = 5
        n = int(randint(0,max_number_of_elements) % max_number_of_elements + 2);
        print(n)
        max_value = 100000
        list_of_intgers = []

        for i in range(n):
            list_of_intgers.append(randint(0,max_value))

        res1 = max_pairwise_product(list_of_intgers)
        res2 = max_pairwise_product_fast(list_of_intgers)
        print(list_of_intgers)

        if (res1 != res2):
            
            print("Wrong , ",res1," ",res2)
            break
        else:
            print("OK")
"""
