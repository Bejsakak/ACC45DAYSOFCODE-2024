def is_expert(T, test_cases):
    results = []
    for X, Y in test_cases:
        if Y * 2 >= X:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Getting results
results = is_expert(T, test_cases)

# Output results
for result in results:
    print(result)
