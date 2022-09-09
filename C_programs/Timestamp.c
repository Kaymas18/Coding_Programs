/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

  
void delay(int number_of_seconds)
{
    // Converting time into milli_seconds
    int milli_seconds = 1000 * number_of_seconds;
  
    // Storing start time
    clock_t start_time = clock();
  
    // looping till required time is not achieved
    while (clock() < start_time + milli_seconds)
        ;
}

int main()
{
    int framesize, sent = 0, ack, i;
    time_t t;   // not a primitive datatype
    time(&t);
    printf("Enter the number of frames \n");
    scanf("%d", &framesize);
    while(1){
        for(i=0;i<framesize;i++){
            
            printf(",\t \n frame %d has been transmitted at %s",sent,ctime(&t));
            
            sent++;
            if(sent == framesize)
            delay(20);
            break;
            
        }
    printf("\n please enter the last ack received \n");
    scanf("%d", &ack);
    if(ack>= framesize)
    break;
    else
    sent = ack;
    }

    return 0;
}