# python3
import sys


def compute_min_refills(distance,n ,tank, stops):
    num_refills = 0
    current_refill = 0
    x = stops
    x.insert(0,0)
    x.append(distance)
    while (current_refill <= n):
    	last_refill = current_refill
    	#greedy choice which is a safe move 
    	while ((current_refill<= n) and (x[current_refill+1]-x[last_refill]<=tank)):
    		current_refill = current_refill + 1

    	if (current_refill == last_refill):
    		return -1
    	
    	if current_refill <= n:
    		num_refills = num_refills + 1

    return num_refills

if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, n, m, stops))
