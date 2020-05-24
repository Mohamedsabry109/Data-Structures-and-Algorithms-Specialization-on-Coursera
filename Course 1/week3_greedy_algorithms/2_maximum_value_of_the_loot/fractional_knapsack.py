# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.   
    values_weights = [i / j for i, j in zip(values, weights)] 
    for i in range(len(weights)):
    	if capacity == 0:
    		return value

    	#get the max value per weight
    	max_ = 0
    	max_loc = 0
    	for i in range(len(weights)):
    		if (values_weights[i]>max_ and weights[i]>0):
    			max_ = values_weights[i]
    			max_loc = i

    	a = min(weights[max_loc],capacity)
    	value = value + a * values_weights[max_loc]
    	weights[max_loc] = weights[max_loc] - a
    	capacity = capacity - a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
