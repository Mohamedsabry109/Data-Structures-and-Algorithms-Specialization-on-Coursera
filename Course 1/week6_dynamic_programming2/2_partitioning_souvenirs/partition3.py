# Uses python3
import sys
import itertools

def partition3(A):
    # for c in itertools.product(range(3), repeat=len(A)):
    #     sums = [None] * 3
    #     for i in range(3):
    #         sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

    #     if sums[0] == sums[1] and sums[1] == sums[2]:
    #         return 1

    # return 0
    import numpy as np
    total_sum = sum(A)
    if len(A) < 3 or total_sum % 3:
        return 0
    subset_sum = total_sum // 3
    matrix = np.zeros((subset_sum+1,len(A)+1))

    for i in range(1, subset_sum+1): 
        for j in range(1, len(A)+1): 
            ii = i - A[j - 1]     
            if A[j - 1] == i or (ii > 0 and matrix[ii][j - 1]): 
                matrix[i][j] = 1 if matrix[i][j - 1] == 0 else 2 
            else:
                matrix[i][j] = matrix[i][j - 1]

    return 1 if matrix[-1][-1] == 2 else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

