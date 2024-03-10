#include <stdio.h>
#include <stdlib.h>
int InSort(int A[], int n)
{
    int i, j, Temp;
    for (i = 1; i <= n; i++)
    {
        Temp = A[i];
        j = i - 1;
        while (Temp < A[j])
        {
            A[j + 1] = A[j];
            j--;
            if (j == -1)
                break;
        }
        A[j + 1] = Temp;
    }
    return 0;
}
