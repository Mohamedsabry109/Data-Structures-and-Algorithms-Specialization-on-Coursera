# Uses python3
import sys

def binary_search(a, x, low , high):
    
    if (high < low):
        return -1
    mid = int(low + (high - low)/2)
    # print(" ")
    # print("searching for ", x)
    # print("a is ",a)
    # print("mid is ",mid)
    # print("high is ",high)
    # print("low is ",low)
    # print("a[mid] = ",a[mid-1])
    # print(" ")
    if a[mid-1] == x :
        return mid-1
    elif x < a[mid-1]:
        return binary_search(a,x,low,mid-1)
    else: 
        return binary_search(a,x,mid+1,high)




def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x , 1 , len(a)), end = ' ')
