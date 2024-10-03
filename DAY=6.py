def max_points(X, Y):
    # Points for Problem A and B
    points_A_start = 500
    points_B_start = 1000
    
    # Attempting A first, then B
    time_A_first = X + Y
    score_A_first = points_A_start - (X * 2) + (points_B_start - (time_A_first * 4))
    
    # Attempting B first, then A
    time_B_first = Y + X
    score_B_first = points_B_start - (Y * 4) + (points_A_start - (time_B_first * 2))
    
    # Return the maximum score
    return max(score_A_first, score_B_first)

def main():
    T = int(input())
    results = []
    for _ in range(T):
        X, Y = map(int, input().split())
        results.append(max_points(X, Y))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
