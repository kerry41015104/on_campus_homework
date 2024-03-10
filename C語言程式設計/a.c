int cmp_int(const void* _a , const void* _b)
{
    int* a = (int*)_a;    //強制型別轉換
    int* b = (int*)_b;
    return *a - *b;
}

qsort(num,任意n,sizeof(num[0]),cmp_int);