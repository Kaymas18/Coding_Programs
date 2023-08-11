#include<stdio.h>
int main()
{
    long long int m=0,tc=0,th=0,t,s=0;
    scanf("%d",&t);
    while(t>0)
    {
        scanf("%lld %lld %lld",&m,&tc,&th);
        s=th-tc;
        if(s%3==0 && m>=s/3)
        {
            printf("No");
        }
        else
        {
            printf("Yes");
        }
        printf("\n");
        s=0;
        m=0;
        tc=0;
        th=0;
        t--;
    }
    return 0;
}