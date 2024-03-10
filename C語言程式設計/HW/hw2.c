#include <stdio.h>



int main() {
    int begin, end, step;
    int kg = 0;
    
    scanf("%d %d %d", &begin, &end, &step);
    
    
    printf("公斤\t    台斤\n");
    
    
    

    for (int kg = begin;kg < end ; kg += step) {
        
        printf("%d\t%5.2f\n",kg ,kg * 1.66);
    }
    
    while (scanf("%d", &kg) != EOF && kg >= 0) {
        
            printf("%4.2f\n", kg * 1.66);
            
               
        
    }        
    return 0;
}