def minimum_attacks(test_cases):
    results = []
    for H, X, Y in test_cases:
        # Option 1: Attack normally until the boss's health is 0 or below
        normal_attacks = (H + X - 1) // X  # Equivalent to ceil(H / X)

        # Option 2: Use the special attack once, then normal attacks
        remaining_health_after_special = H - Y
        if remaining_health_after_special <= 0:
            # If the special attack is enough to defeat the boss
            attacks_with_special = 1
        else:
            # Calculate the number of normal attacks needed after using special
            normal_attacks_after_special = (remaining_health_after_special + X - 1) // X
            attacks_with_special = 1 + normal_attacks_after_special  # 1 for the special attack

        # Take the minimum of both options
        min_attacks = min(normal_attacks, attacks_with_special)
        results.append(min_attacks)
    
    return results

# Read input
T = int(input())
test_cases = []
