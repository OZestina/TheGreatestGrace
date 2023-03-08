#include <stdio.h>
#include <pthread.h>  //컴파일 시 -pthread 필요

int sum = 0;
pthread_mutex_t mutex;

void *counter(void *param)
{
	int i;
	for (i = 0; i < 100000; i++)
	{
		//entry
		pthread_mutex_lock(&mutex);
		
		//critical
		sum++;
		
		//exit
		pthread_mutex_unlock(&mutex);
		
		//remainder
	}
	pthread_exit(0);
}

int main()
{
	pthread_t tid1, tid2;
	pthread_mutex_init(&mutex, NULL);
	
	pthread_create(&tid1, NULL, counter, NULL);
	pthread_create(&tid2, NULL, counter, NULL);
	pthread_join(tid1, NULL);	//wait for tid1
	pthread_join(tid2, NULL);
	printf("%d\n", sum);
}
