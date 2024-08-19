# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def get_lowest_end(segments): # pass the functionality
    lowest_end = float('inf')
    for segment in segments:
        if segment.end < lowest_end:
            lowest_end = segment.end
    return lowest_end

def is_in_segment(num, segment): # pass the functionality
    if segment.start <= num <= segment.end:
        return True
    return False

def get_new_segment(num, segment_list): # pass the functionality
    to_keep = []
    for segment in segment_list:
        if not is_in_segment(num, segment):
            to_keep.append(segment)
    return to_keep

def optimal_points(segments):
    points = []
    while len(segments) > 0:
        lowest_end = get_lowest_end(segments)
        segments = get_new_segment(lowest_end, segments)
        points.append(lowest_end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
