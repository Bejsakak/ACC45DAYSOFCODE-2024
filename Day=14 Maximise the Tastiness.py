def maximize_tastiness(test_cases):
    results = []
    for a, b, c, d in test_cases:
        # Calculate all possible tastiness combinations
        tastiness_A_C = a + c
        tastiness_A_D = a + d
        tastiness_B_C = b + c
        tastiness_B_D = b + d
        
        # Find the maximum tastiness
        max_tastiness = max(tastiness_A_C, tastiness_A_D, tastiness_B_C, tastiness_B_D)
        results.append(max_tastiness)
    
    return results

# Input reading
T = int(input("Enter number of test cases: "))
test_cases = []

for _ in range(T):
    a, b, c, d = map(int, input().split())
    test_cases.append((a, b, c, d))

# Get the results
results = maximize_tastiness(test_cases)

# Output results
for result in results:
    print(result)