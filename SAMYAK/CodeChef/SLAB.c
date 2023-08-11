#include<stdio.h>
int main()
{
	int t,n,s=0,y,z,w,a,b,c;
	//printf("Enter t:");
	scanf("%d",&t);
	while(t>0)
	{
		y=250000;
		z=500000;
		w=750000;
		a=1000000;
		b=1250000;
		c=1500000;
		s=0;
		//printf("Enter n:");
		scanf("%d",&n);
			if(n<=250000)
			{
				s=n;
			}
			else if(n>=250001 && n<=500000)
			{
				s= n-((n-y)*0.05);
			}
			else if(n>=500001 && n<=750000)
			{
				s= n - ((z-y)*0.05 + (n-z)*0.1);
			}
			else if(n>=750001 && n<=1000000)
			{
				s= n - ((z-y)*0.05 + (w-z)*0.1 + (n-w)*0.15);
			}
			else if(n>=1000001 && n<=1250000)
			{
				s= n - ((z-y)*0.05 + (w-z)*0.1 + (a-w)*0.15 + (n-a)*0.2);
			}
			else if(n>=1250001 && n<=1500000)
			{
				s= n - ((z-y)*0.05 + (w-z)*0.1 + (a-w)*0.15 + (b-a)*0.2 + (n-b)*0.25);
			}	
			else
			{
				s= n - ((z-y)*0.05 + (w-z)*0.1 + (a-w)*0.15 +(b-a)*0.2 + (c-b)*0.25 + (n-c)*0.3);
			}
		printf("%d",s);
		printf("\n");
		t--;
	}
}