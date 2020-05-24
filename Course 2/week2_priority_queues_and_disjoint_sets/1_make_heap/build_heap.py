# python3
import random

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def parent(i):
    return (i-1)//2

def right_child(i):
    return 2*i+2

def left_child(i):
    return 2*i+1

def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b


def sift_down(i,data,swaps):
    max_index = i
    l = left_child(i)
    if l < len(data) and data[l] < data[max_index]:
        max_index = l
    r = right_child(i)
    if r < len(data) and data[r] < data[max_index]:
        max_index = r
    if i != max_index:
        data[i], data[max_index] = swap(data[i], data[max_index])
        swaps.append((max_index,i))
        sift_down(max_index,data,swaps)

def sift_up(i,data):
    while i > 0 and data[i] < data[parent(i)]:
        data[i], data[parent(i)] = swap(data[i], data[parent(i)])
        i = parent(i)

def build_min_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    for i in range(len(data)//2 , -1, -1):
        sift_down(i,data,swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_min_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

####STRESS TEST
    # cont = True
    # while cont:
    #     print(".",end="")
    #     n = random.randint(0,1000)
    #     data = []

    #     while len(data) != n:
    #         data.append(random.randint(0,10000))
    #     x_data = data
    #     y_data = data
    #     x = build_heap(x_data)
    #     y =  build_min_heap(y_data)
    #     if (x_data != y_data):
    #         print("Error")
    #         print("data iss : ",data)
    #         print("build_heap ", x)
    #         print("build_min_heap", y)
    #         cont = False


if __name__ == "__main__":
    main()
