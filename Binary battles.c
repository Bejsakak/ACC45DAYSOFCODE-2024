#include <stdio.h>

int main() {
    int T; // Number of test cases
    scanf("%d", &T);
    
    while (T--) {
        int N, A, B;
        scanf("%d %d %d", &N, &A, &B);
        
        // Calculate the number of rounds
        int rounds = 0;
        while (N > 1) {
            rounds++;
            N /= 2;
        }
        
        // Total time calculation
        int total_time = (rounds * A) + ((rounds - 1) * B);
        
        // Output the result
        printf("%d\n", total_time);
    }
    
    return 0;
}