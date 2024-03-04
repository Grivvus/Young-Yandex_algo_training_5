#include <stdio.h>
void make_not_even(int n, int* nums){
    long long res = *nums;
    for(int i=1; i<n; i++){
        if (res % 2 != 0 && *(nums+i) % 2 != 0){
            res *= *(nums+i);
            printf("x");
        }
        else{
            res += *(nums+i);
            printf("+");
        }
    }
    printf("\n");
}

int main(void){
    int n;
    scanf("%d", &n);
    int nums[n];
    for(int i=0; i<n; i++){
        scanf("%d", nums+i);
    }
    make_not_even(n, nums);
    return 0;
}