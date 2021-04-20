#include<pthread.h>
#include <stdio.h>
#include<stdlib.h>
#include<string.h>


/*   ************************************************************   */
/* A program using Threads:

		error check for the appropriate number of command line arguments	

        thread 1: calculates the factorial of the sum of the second command line argument
		and the 3rd command line argument 

		thread 2 prints the extension of the 4th command line argument
		a file name (if there is no file extension and appropriate
		message is displayed


		                                                         */
/*                                                                     */
/* **************************************************************** */
 


int fact;/* thread stores result here */
void *factorial(void *param);		  /* the thread */
void *extension(void *param);
int main (int argc, char *argv[])
{
	pthread_t tid, tid2;		/* thread identifier */
	int retcode;
	long sum;
	int t1;
	int t2;
	char *check="";
	
	if(strstr(argv[3], ".") == NULL) {
	printf(" file does not contain extension \n");
    exit(0);
	}
	if (argc != 4)
	{
	 printf(" invalid number of arguments about to exit!!!!!!!!!!!!\n");
	 exit(0);
	}

													/* insert check input parameters */
	if( atoi(argv[1]) ==0 && atoi(argv[2])==0 )       // this happens if letters are inputted, if only 1 is a number 
	{												  // then just do that one number i guess?
		printf(" please input valid numbers");
		exit(0);
	}
	
                                                       // insert the sume of the second and third command line argument
	check=argv[3];
	t1=atoi(argv[1]);
	t2=atoi(argv[2]);
	sum=t1+t2;
	printf("\n sum: %lu\n", sum);
        /* create the factorial thread */

	retcode = pthread_create(&tid,NULL,factorial,(void*) sum);
	if (retcode != 0) {
		fprintf (stderr, " Unable to create thread\n");
		exit (1);
	}
	
                                                           /* insert code to create the file extension thread */
	retcode = pthread_create(&tid2, NULL, extension, argv[3]);
	if(retcode != 0)
	{
		fprintf(stderr, " Unable to create thread\n");
		exit(1);
	}

                                                  	/* insert code to ensure the parent waits for child threads */
	pthread_join(tid,NULL);
	pthread_join(tid2,NULL);

	printf (" In the parent: the factorial of the sum off the 2nd and 3rd command line arguments  = %d\n \n", fact);
} //main





/* The thread to print the file extension */
void *extension(void *param)
{
    
	
         //code to cast the argument passed to the thread
	
        char * p = (char*)param;
		char * c = (char*)param;
 
		
		int correct=0;



	printf("\n im child 2, the 4th command line aregumet is %s\n",p);

	while(*c != '\0')
	{
		if (*c=='.')
		{
		correct++;
		}
			c++;
		}
		if(correct!=1)
		{
			printf("No Extension Found");
			pthread_exit(0);
	}

	
	while(*p != '.')
	{
		p++;
	}
	
	printf(" the extension of the file is: ");
	p++;
	while(*p != '\0')
	{
		printf("%c", *p);
		p++;
	}
	
	printf("\n"); // insert code to print the file extension


	/* next line is not really necessary */
	pthread_exit(0);
}

/* The thread to get the factorial */
void *factorial(void *param)
{
        
         //cast the argument passed to the thread to long integer
        int i = (int)param;
        int factorial=1;
		printf (" I am child 1, passed value %d\n", i);
		
		
	// insert code to determine the factorial
		while(i > 1)
		{
			factorial=factorial*i;
			i--;
		}
		fact = factorial; 

	/* next line is not really necessary */
	pthread_exit(0);
}


