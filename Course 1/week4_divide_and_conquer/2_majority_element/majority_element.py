# Uses python3
import sys
# using recursion, T(n) = 2T(n/2) + 2n
# by the master theorm we can prove that the complexity is theta(nlog(n))

def get_majority_element(a, left, right):


    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    #mid =  (left + right - 1) // 2 + 1
    mid = int(left + (right-left)/2)
    left_element = get_majority_element(a, left,mid)
    right_element = get_majority_element(a, mid, right)

    
    left_count = sum(1 for i in range(left,right) if a[i]==left_element)
    if ( left_count > (right - left) //2):
        return left_element 

    right_count = sum(1 for i in range(left,right) if a[i]==right_element)
    if (right_count > (right - left) //2):
        return right_element 


    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
