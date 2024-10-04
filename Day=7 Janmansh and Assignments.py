T = int(input())

for _ in range(T):
    # Read the starting time X
    X = int(input())
    
    # Check if he can complete the assignments on time
    if X + 3 <= 10:
        print("Yes")
    else:
        print("No")