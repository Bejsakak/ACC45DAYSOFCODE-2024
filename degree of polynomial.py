def find_polynomial_degree(test_cases):
    results = []
    for case in test_cases:
        N, coefficients = case
        degree = -1  # Initialize degree to -1 (no degree)
        
        # Iterate through coefficients in reverse order to find the highest non-zero coefficient
        for i in range(N - 1, -1, -1):
            if coefficients[i] != 0:
                degree = i
                break
                
        results.append(degree)
    return results

# Input reading
T = int(input("Enter number of test cases: "))
test_cases = []

for _ in range(T):
    N = int(input("Enter number of terms in the polynomial: "))
    coefficients = list(map(int, input("Enter coefficients: ").split()))
    test_cases.append((N, coefficients))

# Find degrees of all test cases
degrees = find_polynomial_degree(test_cases)

# Output results
for degree in degrees:
    print(degree)
