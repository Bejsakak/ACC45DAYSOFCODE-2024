# Read the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the decisions of the referees
    decisions = list(map(int, input().split()))
    
    # Check if all referees agree that the ball is IN (all decisions must be 0)
    if all(decision == 0 for decision in decisions):
        print("IN")
    else:
        print("OUT")
