# Uses python3
import sys

def get_best_item(weights, values): #w=[0, 3, 2], v=[3, 3, 2]
    best_index = 0
    best_value = 0
    for i, weight in enumerate(weights):
        if weight > 0:
            value_per_weight = values[i] / weight
            if value_per_weight > best_value:
                best_value = value_per_weight
                best_index = i
    return best_index

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    amount = [0 for _ in weights]
    for _ in range(len(weights)):
        if capacity <= 0:
            return value
        best_index = get_best_item(weights, values)
        a = min(weights[best_index], capacity)
        value = value + a * values[best_index] / weights[best_index]
        amount[best_index] = a
        weights[best_index] -= a
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))
