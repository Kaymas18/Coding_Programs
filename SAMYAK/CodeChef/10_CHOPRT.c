#include <stdio.h>
int main()
{
    long int t, n1, n2;
    scanf("%lu", &t);
    while (t > 0)
    {
        scanf("%lu", &n1);
        scanf("%lu", &n2);
        if (n1 > n2)
        {
            printf(">\n");
        }
        else if (n1 < n2)
        {
            printf("<\n");
        }
        else
        {
            printf("=\n");
        }
        n1 = 0;
        n2 = 0;
        t--;
    }
}