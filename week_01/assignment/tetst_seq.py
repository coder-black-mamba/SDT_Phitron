from collections import Counter

def min_removals_to_good_sequence(N, A):
    freq = Counter(A)  # Count occurrences of each number
    removals = 0
    print(freq)
    for x, count in freq.items():
        print(x,count)
        if count > x:
            removals += (count - x)  # Remove the extra occurrences
        elif count < x:
            removals += count  # Remove all occurrences of x
    
    print(removals)

# Input handling
N = int(input().strip())
A = list(map(int, input().strip().split()))
min_removals_to_good_sequence(N, A)
