# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    end = False
    i = 1
    while(not end):
    	x = n - i
    	if (x > i):
    		summands.append(i)
    		n = n - i
    		i = i +1
    	else:
    		summands.append(n)
    		end = True

    return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
    input = input()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
