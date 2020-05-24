# Uses python3
import sys

#This is not an optimal solution it has a relatively high space complexity,
#but it's general for multiplying arbitrarly numbers, but still not general for adding arbitrarly numbers
def optimal_sequence(n):
    ops = [3,2,1]
    sequence = []
    min_num_ops = [n+1]*(n+1)
    min_num_ops[0] = 0
    min_num_ops[1] = 0
    sequence.append([0])
    sequence.append([1])
    for num in range(2,n+1):
        sequence.append([])
        for op in ops:
            if (num%op == 0):
                if (op == 1):
                    num_ops = min_num_ops[num - 1] + 1
                    if (num_ops < min_num_ops[num]):
                        min_num_ops[num] = num_ops
                        sequence[num] = sequence[num - 1].copy()
                        sequence[num].append(num)
                else:
                    num_ops = min_num_ops[int(num / op)] + 1
                    if (num_ops < min_num_ops[num]):
                        min_num_ops[num] = num_ops
                        sequence[num] = sequence[int(num / op)].copy()
                        sequence[num].append(num)
    if n>=2 :
        return sequence[num]
    else:
        return [1]


#input = sys.stdin.read()
input = input()
n = int(input)
#sequence = list(optimal_sequence(n))
sequence = optimal_sequence(n)
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
