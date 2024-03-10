#include <stdio.h>
#include <ctype.h>
#define in 0
#define out 1
int main() {
    int WordCount=0, LineCount=0, ByteCount=0,WordLength=0;
    int maxLength=0;
    int c;
    int state = out;
    while ((c=getchar()) != EOF) {
        ByteCount++;
        if (c == '\n') {
            if (state == in) {
                WordCount++;
            }
            state = out;      
            LineCount++;
        }
        else if (isalpha(c) || isdigit(c)) {
            if (state == out) {
                WordLength = 1;
            }
            else {
                WordLength++;
            }        
            state = in;           
        }
        else if (c == ' ' || c == '&' || c == ',' || c== '.' || c == 39 || c == '-') {
            if (state == in) {
                if (WordLength > maxLength) {
                    maxLength = WordLength;
                }    
                WordCount++;
            state = out;
            }
        }
    }        
    printf("Longest Word Length: %d\nWord Count: %d\nLine Count: %d\nByte Count: %d\n", maxLength, WordCount, LineCount, ByteCount);        
    return 0;
}    
 