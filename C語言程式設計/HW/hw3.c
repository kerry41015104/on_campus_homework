#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int main() {
    int alphaCnt[26];
    double alphaRatio[26];
    int digitCnt[10];
    double digitRatio[10];
    int total=0;
    int i, j;
    int c = 0;
    int idx;
    int idx2;
    int maxCntIdx = 0, minCntIdx = 0;
    int maxCnt, minCnt, minCnt2;
    for (i=0;i < 26;i++) {
        alphaCnt[i] = 0;
    }    
    for (j=0;j < 10;j++) {
        digitCnt[j] = 0;
    }
    while (( c = getchar()) != '\n') {
        if (c >= '0' && c <= '9') {
            idx2 = c -'0';
            digitCnt[idx2] +=1;
            total ++;
        }
        if (isalpha(c)) {
            if (isupper(c)) {
                idx = c - 'A';
                alphaCnt[idx] += 1;
            } else {
                idx = c - 'a';
                alphaCnt[idx] += 1;
            }
            total ++;
        }    
    }    
    
    printf("Alphabet statistics:\n");
    for (i = 0;i < 26;i ++) {
        alphaRatio[i] = (double) alphaCnt[i] / total;
    }    
    for (i = 0;i < 26;i ++) {
        printf("%c:\t%d\t%.4f\n", 'a' + i, alphaCnt[i], alphaRatio[i]);
    }
    printf("Number statistics:\n");
    for (j =0;j< 10;j++) {
        digitRatio[j] = (double) digitCnt[j] / total;
    }
    for (j =0;j < 10;j++) {
        printf("%d:\t%d\t%.4f\n", j, digitCnt[j], digitRatio[j]);
    }
    printf("Most frequently number:\n");
    maxCnt = digitCnt[0];
    for (j = 0;j < 10; j++) {
        if (digitCnt[j] > maxCnt) {
            maxCnt = digitCnt[j];
            maxCntIdx = j;
        }
    }
    printf("%d:\t%d\n", maxCntIdx, maxCnt);
    printf("Least frequently number:\n");
    minCnt = digitCnt[0];
    for (j = 0;j < total; j++) {
        for (i=0;i<j;i++) {
            if (digitCnt[i] > digitCnt[i+1]) {
                minCnt2 = digitCnt[j];
                digitCnt[i] = digitCnt[i+1];
                digitCnt[i+1] = minCnt2;
                
                      
            }
            
        }    
            
    for(j=0;j<total;j++) {           
        printf("%d:\t%d\n",abs(total-1-9) , digitCnt[j]); 
    }                   
                    
                
                  
            
       
             
       
                
            
           
            
                
            
            
                 
     
        
        
    }
    
    
    
    return 0;
}
