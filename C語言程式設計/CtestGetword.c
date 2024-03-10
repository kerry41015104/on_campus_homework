#include<stdio.h>
#include<string.h>
#include<ctype.h>
#define Maxlinelen 4096
#define MaxWordlen 128
char *getword(char *text, char *word) {
    char *ptr = text;
    char *qtr = word;
    while (*ptr && isspace(*ptr)) {ptr++;}
    while (*ptr && !(isspace(*ptr))) {
        if (qtr-word >= MaxWordlen) {
            fprintf(stderr,"word length 太長\n");
            break;
        }
        *qtr++=*ptr++;
    }
    *qtr = '\0';
    printf("%d\n",qtr);
    printf("%d\n",word);
    printf("%s\n",word);
    if (qtr-word==0) {
        return NULL;
    }
    printf("ptr:%d\n",ptr);
    return ptr;
}
int main() {
    char line[Maxlinelen];
    char word[MaxWordlen];
    char *ptr;
    while (fgets(line,Maxlinelen,stdin)) {
        ptr = line;
        printf("ptr:%d\n",ptr);
        while (ptr=getword(ptr,word)) {
            printf("%s\n", word);
            printf("%d\n",word);
            printf("-----------------------------\n");
        }
    }
    return 0;
}