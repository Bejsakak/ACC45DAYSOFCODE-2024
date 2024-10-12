def minimum_bags_needed(test_cases):
    results = []
    for N, K, M in test_cases:
        capacity_per_bag = K * M
        bags_needed = (N + capacity_per_bag - 1) // capacity_per_bag
        results.append(bags_needed)
    return results

# Read number of test cases
T = int(input())
test_cases = []

# Read each test case
for _ in range(T):
    N, K, M = map(int, input().split())
    test_cases.append((N, K, M))

# Calculate the minimum bags needed
results = minimum_bags_needed(test_cases)

# Print results for each test case
for result in results:
    print(result)
