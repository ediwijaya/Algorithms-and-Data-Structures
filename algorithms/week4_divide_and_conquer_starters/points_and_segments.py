# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    line_array = []
    for s in starts:
        line_array.append((s, 'left'))
    for e in ends:
        line_array.append((e, 'right'))
    for p in points:
        line_array.append((p, 'point'))
    line_array.sort()
    
    counter = 0
    record_dict = {}
    for elm in line_array:
        if elm[1] == 'left':
            counter += 1
        elif elm[1] == 'right':
            counter -= 1
        else:
            record_dict[elm[0]] = counter
    result = [record_dict[p] for p in points]
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')