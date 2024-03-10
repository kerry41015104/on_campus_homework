#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main () {
    int i;
    int *nums = malloc(32*sizeof(int));
    char *buf = malloc(32*sizeof(char));
    char ** data = malloc(32*sizeof(char*));
    for ( i = 0; i < 32; i++)
    {
        *(data+0)= malloc(1024*sizeof(char));
    }

    int i;
    while (fgets(buf,32,stdin) != NULL) {

        strcpy(*(data+i) , buf);
        i++;

    }

    for ( i = 0; i < count; i++)
    {
        /* code */
    }



    return 0;
}