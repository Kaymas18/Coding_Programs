#include <stdio.h>       
int main()    
{    
    int arr[100],n,i,temp = 0,j;    
    scanf("%d",&n);   
    for (i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }   
        for ( i = 0; i < n; i++) {     
        for ( j = i+1; j < n; j++) {     
           if(arr[i] > arr[j]) {    
               temp = arr[i];    
               arr[i] = arr[j];    
               arr[j] = temp;    
           }     
        }     
    }        
    printf("\n");       
    for (i = 0; i < n; i++) {     
        printf("%d ", arr[i]);    
    }    
    return 0;    
}
