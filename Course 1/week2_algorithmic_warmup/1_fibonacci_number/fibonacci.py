# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_table(n):
	
	l = []
	l.append(0)
	l.append(1)
	
	for i in range (n+1):
		l.append(l[i]+l[i+1])
	
	return l[n]

n = int(input())
print(calc_fib_table(n))
