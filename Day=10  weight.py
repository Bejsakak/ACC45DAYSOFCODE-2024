def can_measure_weight(W, X, Y, Z):
    weights = [X, Y, Z]
    # Check all combinations of weights
    for i in range(1, 1 << 3):  # from 1 to 2^3 - 1
        total_weight = 0
        for j in range(3):
            if i & (1 << j):
                total_weight += weights[j]
        if total_weight == W:
            return "YES"
    return "NO"

def main():
    T = int(input())
    results = []
    for _ in range(T):
        W, X, Y, Z = map(int, input().split())
        result = can_measure_weight(W, X, Y, Z)
        results.append(result)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

