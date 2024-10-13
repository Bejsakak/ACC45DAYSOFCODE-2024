def count_notebooks(n):
    # 1 kg of pulp makes 1000 pages
    pages_per_kg = 1000
    # 1 notebook consists of 100 pages
    pages_per_notebook = 100
    # Calculate total pages from N kg of pulp
    total_pages = n * pages_per_kg
    # Calculate number of notebooks
    notebooks = total_pages // pages_per_notebook
    
    return notebooks

# Input number of test cases
T = int(input("Enter number of test cases: "))

# Process each test case
for _ in range(T):
    N = int(input())
    result = count_notebooks(N)
    print(result)
