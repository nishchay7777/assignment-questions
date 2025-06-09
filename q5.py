
from itertools import combinations

n = int(input())             
letters = input().split()     
k = int(input())              

all_combinations = list(combinations(letters, k))

count_with_a = 0
for combo in all_combinations:
    if 'a' in combo:
        count_with_a += 1

probability = count_with_a / len(all_combinations)

print(f"{probability:.3f}")
