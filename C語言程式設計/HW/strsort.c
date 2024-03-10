#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *mystrcpy(char *a,char *b) {
    while (*b) {
        *a++ = *b++;
    }
    *a='\0';
    return a;
}
int main () {
    int i,cnt=0,j,len;
    char *buf = malloc(1024*sizeof(char));
    char *temp = malloc(1024*sizeof(char));
    char ** data = malloc(32*sizeof(char*));
    for ( i = 0; i < 32; i++)
    {
        *(data+i)= malloc(1024*sizeof(char));
    }
    while (fgets(buf,1024,stdin) != NULL) {
        len = strlen(buf);
        if (buf[len-1]=='\n') {
            buf[len-1] = '\0';
        }
        mystrcpy(data[cnt],buf);
        cnt++;
    }
    for(i=0;i<cnt-1;i++){
		for(j=0;j<cnt-1-i;j++){
			if(strcmp(data[j],data[j+1])>0){
				temp=data[j];
				data[j]=data[j+1];
				data[j+1]=temp;
			}
		}
	}
    for (i=0;i<cnt;i++) {
        printf("%s\n",data[i]);
    }
    return 0;
}