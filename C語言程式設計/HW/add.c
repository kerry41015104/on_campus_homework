#include<stdio.h>
int main () {
    int count,i=0;
    int c,d;
    int a;
    int x,b=0;
    while ((scanf("%d", &x)) != EOF) {
        a = x;
        i++;
        count = i %5;
        if (count==1) {
            b = a;
            printf("(State RST) => %d\n", b);
        }
        if (count==2) {
            b = a+b;
            printf("(State ADD) => %d\n", b);
        }
        if (count==3) {
            b=b-a;
            printf("(State SUB) => %d\n", b);
        }
        if (count==4) {
            b=a*b;
            printf("(State MUL) => %d\n", b);
        }
        if (count==0) {
            if (b==0) {
                printf("(State DIV) => division by zero => reset\n");
                i=0;
            }
            else if (b!=0)  {
                b=b/a;
                d=(a/b)*b;
                if (c==d) {
                    printf("(State DIV) => %d\n", c);
                    b=a/b;
                }
                if (c!=d) {
                    printf("(State DIV) => %d\n", 0);
                    b=0;
                }
                i=1;
            }

        }

    }

    return 0;
}