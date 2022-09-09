#include <stdio.h>
int
main () 
{
  
int w, i, f, frame[40];
  
printf ("enter the window size\n");
  
scanf ("%d", &w);
  
printf ("enter the no if frames to transmitted:\n");
  
scanf ("%d", &f);
  
printf ("enter the %d frame", f);
  
for (i = 1; i <= f; i++)
    
scanf ("%d", &frame[i]);
  
printf
    ("\nwith sliding window protocol the frames will be transmitted in folowing manner\n\n");
  
printf ("after sending %d frames at each stage sender waits for ack\n\n",
	   w);
  
 
for (i = 1; i <= f; i)
    
    {
      
if (i % w == 0)
	
	{
	  
printf ("%d \n", frame[i]);
	  
printf ("ack of above frame is recieeved\n\n");
	
 
 
}
      
      else
	
printf ("%d \n", frame[i]);
    
}
  
if (f != 0)
    
printf ("\n ack of above frame sent is reacived by sender\n");
  
return 0;

}
