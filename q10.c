#include <stdio.h>

int fun(int *k)
{
    *k += 4;
    return 3 * (*k) - 1;
}
int main()
{
    int i = 10, j = 10, sum1, sum2;
    sum1 = (i / j) + fun(&j);
    sum2 = fun(&i) + (i / j);

    printf("%d",sum1);
    printf("%d",sum2);

    return 0;
}