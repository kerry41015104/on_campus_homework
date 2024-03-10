#include <stdio.h>
#include <stdlib.h>
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
    for (i = 0; i < n; i++)
    {
        printf("%d\n", list[i]);
    }
    return 0;
}
int main()
{
    int a[10];
    int n = 5;
    int i;
    for (i = 0; i < 5; i++)
    {
        a[i] = rand();
    }
    selection_sort(a, n);
    return 0;
}