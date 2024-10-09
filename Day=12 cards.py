def minimum_flips(test_cases):
    results = []
    for N, X in test_cases:
        # Calculate face-down cards
        face_down = N - X
        # Minimum flips needed
        min_flips = min(X, face_down)
        results.append(min_flips)
    return results

# Read input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = minimum_flips(test_cases)

# Output results
for result in results:
    print(result)
