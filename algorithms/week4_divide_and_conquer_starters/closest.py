#Uses python3
import sys
import math
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def calc_dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)** 2)

def brute_distance(points):
    n = len(points)
    min_dist = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            curr_dist = calc_dist(points[i], points[j])
            if curr_dist < min_dist:
                min_dist = curr_dist
    return min_dist

def closest_within_range(within_range, min_dist):
    within_range.sort(key=lambda point: point.y)
    size = len(within_range)
    for i in range(size):
        for j in range(i+1, size):
            if (within_range[j].y - within_range[i].y) >= min_dist:
                break
            curr_dist = calc_dist(within_range[j], within_range[i])
            if curr_dist < min_dist:
                min_dist = curr_dist
    return min_dist

def minimum_distance(points):
    n = len(points)
    if n <= 3:
        return brute_distance(points)
    
    points.sort(key=lambda point: point.x)
    mid = n // 2
    mid_point = points[mid]
    d1 = minimum_distance(points[:mid])
    d2 = minimum_distance(points[mid:])
    d = min(d1, d2)
    within_range = []
    for i in range(n):
        if abs(points[i].x - mid_point.x) < d:
            within_range.append(points[i])
    return min(d, closest_within_range(within_range, d))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(map(lambda x: Point(x[0], x[1]), zip(x, y)))
    print("{0:.9f}".format(minimum_distance(points)))