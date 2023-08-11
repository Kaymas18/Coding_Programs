#include<stdio.h>
#include<string.h>
int main()
{
    int t,i,sum=0;
    char s[101];
    //printf("Enter t:");
    scanf("%d",&t);
    while(t>0)
    {
        //printf("Enter string");
        scanf("%s",s);
        for(i=0;s[i]!='\0';i++)
        {
            if(s[i]=='b' || s[i]=='c')
            {
                sum=sum+(s[i]-'a');
            }
           else if(s[i]=='d')
            {
                sum=sum+('e'-s[i]);
            }
           else if(s[i]=='f' || s[i]=='g')
            {
                sum=sum+(s[i]-'e');
            }
            else if(s[i]=='h')
            {
                sum=sum+('i'-s[i]);
            }
            else if(s[i]>='j' && s[i]<='l')
            {
                sum=sum+(s[i]-'i');
            }
            else if(s[i]=='m' || s[i]=='n')
            {
                 sum=sum+('o'-s[i]);
            }
            else if(s[i]>='p' && s[i]<='r')
            {
                sum=sum+(s[i]-'o');
            }
            else if(s[i]=='s' || s[i]=='t')
            {
                 sum=sum+('u'-s[i]);
            }
            else if(s[i]>='v' && s[i]<='z')
            {
                sum=sum+(s[i]-'u');
            }
        }
        printf("%d\n",sum);
        sum=0;
        t--;
    }
}