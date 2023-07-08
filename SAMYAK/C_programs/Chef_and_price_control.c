//codechef
//code for PRICECON 
#include<stdio.h>
int main()
{
	int t,n,k,i,s=0,l=0,p[10001],c=0;
	//printf("Enter t:");
	scanf("%d",&t);
	while(t>0)
	{
	s=0;
	l=0;
	//printf("\nEnter n and k:");
	scanf("\n%d %d",&n,&k);
	//printf("Enter k:");
	//scanf("%d",&k);
	//printf("Enter array:");
		for(i=0;i<n;i++)
		{
			scanf("%d",&p[i]);
			s=s+p[i];
		}
		for(i=0;i<n;i++)
		{
			if(k<p[i])
			{
				c=i;
				p[c]=k;	
			}
		l=l+p[i];
		}
	printf("%d\n",s-l);
	t--;
	}
}
