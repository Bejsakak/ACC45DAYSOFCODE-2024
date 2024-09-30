def total_working_hours(test_cases):
    results = []
    for X, Y in test_cases:
        # Calculate total working hours: 4 days of X hours + 1 day of Y hours
        total_hours = (4 * X) + Y
        results.append(total_hours)
    return results

# Read number of test cases
T = int(input())
test_cases = []

# Read each test case
for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

# Calculate and print results
results = total_working_hours(test_cases)
for result in results:
    print(result)
