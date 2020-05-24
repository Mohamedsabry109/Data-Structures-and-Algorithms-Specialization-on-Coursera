# Uses python3
import sys

def get_change(m):
    #write your code here
    counts = 0
    coins = [10,5,1]
    while (m > 0):
    	i = 0
    	while(m < coins[i]):
    		i = i + 1
    	m = m - coins[i]
    	counts = counts + 1
    m = counts

    return m

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
