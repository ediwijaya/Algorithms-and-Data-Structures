# python3
import numpy as np
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyhash(string_list, p, x):
    hash = 0
    for char in reversed(string_list):
        hash = (hash * x + ord(char)) % p
    return hash

def precompute_hashes(text, len_pattern, prime_num, x):
    len_text = len(text)
    hash_list = np.array([None] * (len_text - len_pattern + 1)) # perlu upgrade ke np array
    string_list = text[len_text-len_pattern:] # karena kita akan cari hash dari paling belakang, jadi ambil len(pattern) char paling belakang
    hash_list[len_text - len_pattern] = polyhash(string_list, prime_num, x)
    y = 1
    for _ in range(len_pattern):
        y = (y * x) % prime_num
    for i in range(len_text - len_pattern - 1, -1, -1):
        hash_list[i] = (x * hash_list[i+1] + ord(text[i]) - y * ord(text[i + len_pattern])) % prime_num
    return hash_list

def get_occurrences(pattern, text):
    # Using RabinKarp
    p_prime = 1000000007
    x = random.randint(1, p_prime - 1)
    positions = []

    p_hash = polyhash(pattern, p_prime, x)
    h_list = precompute_hashes(text, len(pattern), p_prime, x)
    for i in range(0, len(text) - len(pattern) + 1):
        if p_hash != h_list[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))