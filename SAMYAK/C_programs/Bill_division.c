//Hackerrank
#include<stdio.h>
int main()
{
	int n,k,bill[100000],b,i,s=0,r=0;
	//printf("Enter the no of items:");
	scanf("%d",&n);
	//printf("The item no she didn't eat:");
	scanf("%d",&k);
	//printf("Enter the bill amount:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&bill[i]);
		if(k!=i)
		{
			s=s+bill[i];
		}
	}
	r=s/2;
	//printf("Enter amount charged from Anna:");
	scanf("%d",&b);
	if(r==b)
	{
		printf("Bon Appetit");
	}
	else
	{
		printf("%d",b-r);
	}
}
