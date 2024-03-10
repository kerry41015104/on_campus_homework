#include <stdio.h>
int selection_sort(int list[], int n)
{
    int i, j, min_id, temp;
    for (i = 0; i < n - 1; i++)
    { //固定i比較
        min_id = i;
        for (j = i + 1; j < n; j++)
        { //跟i換位置
            if (list[j] < list[min_id])
                min_id = j;
        }
        temp = list[i];
        list[i] = list[min_id];
        list[min_id] = temp;
    }
    return 0;
}