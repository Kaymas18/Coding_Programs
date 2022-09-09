#include<stdio.h>
int main()
{
int i, tf, f;
printf("Enter the total no of frame: ");
scanf("%d", &tf);
printf("Send frames:");
for(i=1;i<=tf;i++)
{
printf("%d\n",i);
}
printf("No. of frames recieved: ");
scanf("%d",&f);
printf("Recived frames:");
for(i=1;i<=f;i++)
{
printf("%d\n", i);
}
printf("resend %d frames\n", tf-f);
printf("Recieved frame:"); 
for(i=f+1;i<=tf;i++)
{
printf(" %d\n", i);
}
return 0;
}
