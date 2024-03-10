#include <stdio.h>
#define ture 1
#define false 0
int mysprt (long long x) {
    long long i;
    long long upper;
    int step=1000;
    for (i=0;i*i<=x;i+=step) {}
    if (i*i==x) return i;
    upper=i;
    for (i=upper;i*i>x;i--) {}
    return i;
}
int isprime(long long k) {
    int i,x;
    long long d;
    d=mysprt(k);
    for (i=2;i<d;i++) {
        x = k/i *i;
        if (x == k) return false;
    }
    return ture;
}
int main() {
    long long k;
    while ((scanf("%lld", &k)) != EOF) {
        if (isprime(k)) {
            printf("is_prime");
        }
        else {
            printf("is_not_prime");
        }
    }
    return 0;
}
