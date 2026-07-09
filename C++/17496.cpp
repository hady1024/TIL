#include <stdio.h>

int main () {
    int N, T, C, P;
    scanf("%d %d %d %d", &N, &T, &C, &P);
    printf("%d", (N-1) / T * C * P)
    return 0;
}

