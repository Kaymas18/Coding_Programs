//Codechef
#include<stdio.h>
void main()
{
    int t,n,k,d,a[100],i,s=0,p=0;
    scanf("%d",&t);
    while(t>0)
    {
        scanf("%d %d %d",&n,&k,&d);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            s=s+a[i];
        }
        p=s/k;
        if(p==0)
        {
            printf("0\n");
        }
        else if(p>d)
        {
            printf("%d\n",d);
        }
        else 
        {
            printf("%d\n",p);
        }
        for(i=0;i<n;i++)
        {
            a[i]=0;
        }
        p=0;
        i=0;
        n=0;
        k=0;
        s=0;
        d=0;
        t--;
    }
}