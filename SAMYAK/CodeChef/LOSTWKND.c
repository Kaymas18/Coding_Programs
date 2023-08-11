#include<stdio.h>
int main()
{
	int t,a[6],p,i,s;
	//printf("Enter t:");
	scanf("%d",&t);
	while(t>0)
	{
		s=0;
		p=0;
		//printf("Enter array:");
		for(i=0;i<5;i++)
		{
			scanf("%d",&a[i]);
			s=s+a[i];
		}
		//printf("Enter p:");
		scanf("%d",&p);
		if(s*p>120)
		{
			printf("Yes");
		}
		else
		{
			printf("No");
		}
		printf("\n");
		t--;
	}
}