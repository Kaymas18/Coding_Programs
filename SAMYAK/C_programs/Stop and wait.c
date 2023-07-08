#include<stdio.h>
int main ()
{
  int framesize, sent = 0, ack, i;
  printf ("Enter the number of frames \n");
  scanf ("%d", &framesize);
  while (1)
    {
      for (i = 0; i < framesize; i++)
	{
	  printf (",\t \n frame %d has been transmitted", sent);
	  sent++;
	  if (sent == framesize)
	    break;
	}
      printf ("\n please enter the last ack received \n");
      scanf ("%d", &ack);
      if (ack >= framesize)
	break;
      else
	sent = ack;
    }

  return 0;
}
