/*GFG
User function Template for python3
Love babbar DSA Sheet Question 4 of array
Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
*/
//{ Driver Code Starts
//Initial Template for C
#include <stdio.h>
// } Driver Code Ends
//User function Template for C

void sort012(int a[], int n)
{
    int c=0,d=0,e=0,i,l=0;
    for(i=0;i<n;i++)
    {
        if(a[i]==0){c=c+1;}
        else if(a[i]==1){d=d+1;}
        else{e=e+1;}}
    for(i=0;i<c;i++){a[l++]=0;}
    for(i=0;i<d;i++){a[l++]=1;}
    for(i=0;i<e;i++){a[l++]=2;}
}

//{ Driver Code Starts.

int main() {

    int t;
    scanf("%d", &t);

    while(t--){
        int n;
        scanf("%d", &n);
        int arr[n];
        for(int i=0;i<n;i++){
            scanf("%d", &arr[i]);
        }

        sort012(arr, n);

        for (int i = 0; i < n; i++)
            printf("%d ", arr[i]);
        printf("\n");
    }
    return 0;
}

// } Driver Code Ends