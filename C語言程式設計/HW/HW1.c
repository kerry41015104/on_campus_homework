#include <stdio.h>
#include <string.h>
#include <stdlib.h>



int main() {
    char input[30];
    
    char question1[] = "電腦";
    char question2[] = "鑰匙";
    char question3[] = "程式碼";
    char question4[] = "當掉";
    char question5[] = "陣列";
    char question6[] = "記憶體區段錯誤";
    char question7[] = "匯流排錯誤";
    char question8[] = "字元";
    char question9[] = "整數";
    char question10[] = "浮點數";
    char answer1[] = "computer";
    char answer2[] = "key";
    char answer3[] = "code";
    char answer4[] = "flunk";
    char answer5[] = "array";
    char answer6[] = "segmentation fault";
    char answer7[] = "bus error";
    char answer8[] = "character";
    char answer9[] = "integer";
    char answer10[] = "floating point";
    while(scanf("%s", input) != EOF) {
        if (strcmp(input, question1) == 0 ) {
            printf("%s\n", answer1);    
        }  
        else if (strcmp(input , question2) == 0) {
            printf("%s\n", answer2);    
        }
        else if (strcmp(input , question3) == 0) {
            printf("%s\n", answer3);    
        }    
        else if (strcmp(input , question4) == 0) {
            printf("%s\n", answer4);    
        }    
        else if (strcmp(input , question5) == 0) {
            printf("%s\n", answer5);    
        }    
        else if (strcmp(input , question6) == 0) {
            printf("%s\n", answer6);    
        }    
        else if (strcmp(input , question7) == 0) {
            printf("%s\n", answer7);    
        }    
        else if (strcmp(input , question8) == 0) {
            printf("%s\n", answer8);    
        }    
        else if (strcmp(input , question9) == 0) {
            printf("%s\n", answer9);    
        }    
        else if (strcmp(input , question10) == 0) {
            printf("%s\n", answer10);
        }
        else { printf("這啥鬼?");    
        }    
    }
    return 0;
}          