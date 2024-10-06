def cooler_dilemma(test_cases):
    results = []
    for x, y in test_cases:
        if x >= y:
            results.append(0)  # Cannot rent if cost is equal or greater than purchase
        else:
            max_months = (y - 1) // x  # Calculate maximum months of renting
            results.append(max_months)
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    x, y = map(int, input().split())
    test_cases.append((x, y))

# Get results
results = cooler_dilemma(test_cases)

# Print output
for result in results:
    print(result)
