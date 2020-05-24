# Uses python3
def edit_distance(s, t):
    #write your code here

    n = len(s) + 1  # rows
    m = len(t) + 1  # cols
    a = [0] * n
    
    for i in range(n):
    	a[i] = [0] * m
    #filling the rows
    for i in range(n):
    	a[i][0] = i
    #filling columns
    for i in range(m):
    	a[0][i] = i

    for j in range(1,m):
    	for i in range(1,n):
    		insertion = a[i][j-1] + 1  
    		deletion = a[i-1][j] + 1
    		match = a[i-1][j-1]
    		mismatch = a[i-1][j-1] + 1
    		if s[i-1] == t[j-1]:
    			a[i][j] = min(insertion,deletion,match)
    		else:
    			a[i][j] = min(insertion,deletion,mismatch)

    return a[n-1][m-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
