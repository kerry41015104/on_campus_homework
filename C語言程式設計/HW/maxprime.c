#include <stdio.h>

int main() {


int n;
int isPrime = 1;
printf("Enter a number:\n");
scanf("%d",&n);

for(int i = n;i>0;i--)
{
    isPrime = 1;
    for(int j = 2; j<i;j++) {
        if (i%j == 0 ) {
            isPrime = 0;
            break;
        }
    }
    if(isPrime == 1) {
        printf("%d\n",i);
        break;
        }

}


return 0;
}

