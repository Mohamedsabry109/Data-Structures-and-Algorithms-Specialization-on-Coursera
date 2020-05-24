# Uses python3
import sys
from random import randint


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a, b):
	if (a == 0 or b == 0):
		return a*b
	if (a > b):
		max_ = a
		min_ = b
	else:
		max_ = b
		min_ = a

	for l in range(1, min_+1):
		if max_ * l % min_ == 0:
			break
	return max_ * l


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    print(lcm(a,b))


	# while(True):

	#     max_value = 10000
	#     a = int(randint(0,max_value))
	#     b = int(randint(0,max_value))
	    
	#     print("a : ", a, " b : ",b)

	#     res1 = lcm_naive(a,b)
	#     res2 = lcm(a,b)
	    
	#     #print("a : ", a, " b : ",b)

	#     if (res1 != res2):
	        
	#         print("Wrong , ",res1," ",res2)
	#         break
	#     else:
	#         print("OK")
