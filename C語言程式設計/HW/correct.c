#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
    int i,cnt=0,j=0,len,Correct=0;
    char *buf = malloc(1024*sizeof(char));
    char *s = malloc(1024*sizeof(char));
    char *temp = malloc(1024*sizeof(char));
    char ** data = malloc(32*sizeof(char*));
    double atof ( const char * str );
    while (fgets(buf,1024,stdin) != NULL) {
        len = strlen(buf);
        if (buf[len-1]=='\n') {
            buf[len-1] = '\0';
        }
        s = strtok(buf, " ");
        while(s != NULL) {
            j++;
            data[cnt++]=s;
            s = strtok(NULL, " ");
        }
        double f1=atof(data[0]);
        double f2;
        for (i=0;i<j;i++) {
            if (i%2!=0 ) {
                if (strcmp(data[i],'+')==0) {
                    f1=f1+atof(data[i+1]);
                }
                if (strcmp(data[i],'-') {
                    f1=f1-atof(data[i+1]);
                }
            }
        }
        printf("%f\n", f1);
        if (f1==f2) {
            Correct++;
        }
        printf("%d\n",Correct);
        j=0;
        cnt=0;
    }

   return 0;
 }
