# Uses python3
import sys

def optimal_sequence(n):
    sequence = [[1]]
    for i in range(1, n):
        x = i + 1
        options_mul3 = float('inf')
        options_mul2 = float('inf')
        options_add1 = float('inf')
        if (x % 3 ) == 0:
            mul3_idx = x//3 - 1
            options_mul3 = len(sequence[mul3_idx])
        if (x % 2) == 0:
            mul2_idx = x//2 - 1
            options_mul2 = len(sequence[mul2_idx])
        add1_idx = i - 1
        options_add1 = len(sequence[add1_idx])
        options = [options_mul3, options_mul2, options_add1]
        
        min_ops = min(options)
        min_ops_idx = options.index(min_ops)
        if min_ops_idx == 0:
            prev_step = sequence[mul3_idx]
        elif min_ops_idx == 1:
            prev_step = sequence[mul2_idx]
        else:
            prev_step = sequence[add1_idx]
        min_ops += 1
        sequence.append(prev_step + [x])
    return sequence[-1]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
