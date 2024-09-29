def minimum_total_cost(T, test_cases):
    results = []
    for i in range(T):
        N, X = test_cases[i]
        # Calculate the number of subscriptions needed
        subscriptions_needed = (N + 5) // 6  # This is equivalent to ceil(N / 6)
        # Calculate the total cost
        total_cost = subscriptions_needed * X
        results.append(total_cost)
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    N, X = map(int, input().split())
    test_cases.append((N, X))

# Calculate results
results = minimum_total_cost(T, test_cases)

# Output results
for result in results:
    print(result)