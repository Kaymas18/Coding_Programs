#include<stdio.h>
int main()
{
    int n,temp=0;
    scanf("%d",&n);
    temp=n;
    if(temp%4==0)
    {
        n++;
    }
    else
    {
        n--;
    }
    printf("%d",n);
}