#include <stdio.h>
#define n 100000000000000
long long mysprt (long long x) {
    long long i;
    long long upper,low,mid,z;
    long long step=1;
    i=x/10;
    while (i*i>=x) {
      if (i*i==x) return i;
      i=i/10;
    }
    z=i;
    for (i=z;i*i<=x;i+=step) {
        step= 2*step;
        if (i*i==x) return i;
    }
    upper=i;
    low=i - step;
    while (low < upper-1) {
        mid = (upper+low) /2;
        if (mid*mid==x) return mid;
        else if (mid*mid>x) {
            upper = mid;
        }
        else if (mid*mid<x) {
            low = mid;
        }
    }
}
float mysprt2 (long long x, long long y) {
    float step= 0.1;
    float step2=0.01;
    float i,upper;
    for (i=x;i*i<=y;i+=step) {
        if (i*i==y) return i;
    }
    upper = i;
    for (i=upper;i*i>y;i-=step2) {}
    if (y-i*i > (i+0.01)*(i+0.01)-y) return i+0.01;
    else return i;
}
int main () {
    long long x,q;
    double q2;
    while ((scanf("%lld", &x)) != EOF) {
        if (x>=n) break;
        if (x<1) break;
        q=mysprt(x);
        q2=mysprt2(q,x);
        if (q2 - q != 0) {
            printf("%.2lf\n", q2);
        }
        else {
            printf("%.0lf\n", q2);
        }
    }
    return 0;
}