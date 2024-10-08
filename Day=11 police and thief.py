def minimum_time_to_catch(T, test_cases):
    results = []
    for case in test_cases:
        X, Y = case
        time = abs(Y - X)  # Time is the absolute distance between X and Y
        results.append(time)
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

# Calculate results
results = minimum_time_to_catch(T, test_cases)

# Print output
for result in results:
    print(result)