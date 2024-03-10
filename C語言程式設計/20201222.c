#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ON 1
#define OFF 0
#define INCREASING 1
#define DECREASING -1
#define STRINGSORT 0
#define NUMERICALSORT 1
#define MaxLineLen 4096
#define MaxLineCnt (1<<18)
#define MaxPath 1024
// -r 大到小
// -n numerical sorting
// -h help massage
void mysortNum(char **lines, int lineCnt, int Order) {
    int i,j;
    char *tmp;
    for (i=0;i<lineCnt;i++) {
        for (j=0;j<lineCnt-i-1;j++) {
            if (atoi(lines[j]) * Order> atoi(lines[j+1]) * Order) {
                tmp = lines[j];
                lines[j] = lines[j+1];
                lines[j+1] = tmp;

            }
        }
    }
}
void mysortStr(char **lines, int lineCnt, int Order) {
    int i,j;
    char *tmp;
    for (i=0;i<lineCnt;i++) {
        for (j=0;j<lineCnt-i-1;j++) {
            if (strcmp(lines[j], lines[j+1]) * Order> 0) {
                tmp = lines[j];
                lines[j] = lines[j+1];
                lines[j+1] = tmp;

            }
        }
    }
}
void output(char *lines[], int lineCnt) {
    int i;
    for(i=0;i<lineCnt;i++) {
        printf("%s", lines[i]);
    }
}
void usage(char *progname)
{
    fprintf(stderr, "%s\t[-r -n -h] [textfile]\n", progname);
    fprintf(stderr, "\t-r reverse order\n");
    fprintf(stderr, "\t-n numercial comparison\n");
    fprintf(stderr, "\t-h help massage\n");
}
int main(int argc, char *argv[])
{
    //int Reverse = OFF;
    int Order = INCREASING;
    int SortMode = STRINGSORT;
    int i, ldx;
    char textfile[MaxPath];
    char line[MaxLineLen];
    char *lines[MaxLineCnt];
    FILE *fp;
    textfile[0] = '\0';
    if (argc>1) {
        for (i=1;i<argc;i++) {
            if (argv[i][0] == '-') {
                if (strcmp(argv[i],"-r") == 0) {
                    Order = DECREASING;
                    continue;
                }
                if (strcmp(argv[i],"-n") == 0) {
                    SortMode = NUMERICALSORT;
                    continue;
                }
                if (strcmp(argv[i],"-h") == 0) {
                    usage(argv[0]);
                    exit(1);
                }
                fprintf(stderr, "illegal options: %s\n", argv[i]);
                usage(argv[0]);
                exit(1);
            }
            strcpy(textfile, argv[i]);
            break;
        }
    }
    if(textfile[0] == '\0') {
        fp = stdin;
    }
    else {
        fp = fopen(textfile, "r");
        if(fp == NULL) {
            fprintf(stderr, "fopen error: %s\n", textfile);
            exit(1);
        }
    }
    ldx = 0;
    while (fgets(line, MaxLineLen, fp))
    {
        lines[ldx] = strdup(line);
        ldx++;
    }
    if (SortMode == STRINGSORT) {
        mysortStr(lines, ldx, Order);
    }
    else {
        mysortNum(lines, ldx, Order);
    }
    output(lines, ldx);
    return 0;
}