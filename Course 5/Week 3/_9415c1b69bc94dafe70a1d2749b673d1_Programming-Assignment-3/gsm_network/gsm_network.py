# python3
import itertools

def read():
    n, m = map(int, input().split())
    edges = [ list(map(int, input().split())) for i in range(m)]
    return n, m, edges


def printEquisatisfiableSatFormula(clauses,n):
    print(len(clauses), n*3)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

def varnum(i, k):
    return 3*(i-1) + k
    
def exactlyOneOf(i):
    literals = [varnum(i, k) for k in colors]
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def adj(i, j):
    for k in colors:
        clauses.append([-varnum(i, k), -varnum(j, k)])

n, m, edges = read() 
clauses = []
colors = [1,2,3]

for i in range(1, n+1):
    exactlyOneOf(i)

for i, j in edges:
    adj(i, j)


printEquisatisfiableSatFormula(clauses,n)
