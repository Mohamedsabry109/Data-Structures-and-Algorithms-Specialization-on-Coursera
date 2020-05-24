#Uses python3

import sys

def largest_number(a):
    res = ""
    L = len(a)
    i = 0
    while (i < L):
    	max_digit = 0
    	l = len(a)
    	j = 0
    	while (j < l):
    		#greedy choice, a safe move 
    		if (is_better(a[j],max_digit)):
    			max_digit = a[j]
    		j = j + 1
    	res += str(max_digit)
    	a.remove(str(max_digit))
    	i = i + 1
    return res

def is_better(a,b):
	if (int(str(a)+str(b))>=int(str(b)+str(a))):
		return True
	else:
		return False



if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
