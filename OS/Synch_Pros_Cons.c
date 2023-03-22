#버퍼 하나하나마다 sem_t가 있어야 하는거 아닌가..?
#하기의 코드를 그대로 실행하면 producer가 빠른 속도로 실행됐을 때 인출(consumer 호출)되기 전에 이미 채워져있는 buffer 칸에 또 produce하는 일이 생긴다.. 

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>

#define true 1
#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];

pthread_mutex_t	mutex;
sem_t			empty, full;

int	in = 0, out = 0;

void	insert_item(int item)
{
	sem_wait(&empty);
	pthread_mutex_lock(&mutex);

	buffer[in] = item;
	printf("Producer %d: inserted $%d\n", in, item);
	in = (in + 1) % BUFFER_SIZE;
	

	pthread_mutex_unlock(&mutex);
	sem_post(&full);
}

void	remove_item(int *item)
{
	sem_wait(&full);
	pthread_mutex_lock(&mutex);

	item = buffer[out];
	buffer[out] = 0;
	printf("          Consumer %d: removed $%d\n", out, item);
	out = (out + 1) % BUFFER_SIZE;
	

	pthread_mutex_unlock(&mutex);
	sem_post(&empty);
}

void	*producer(void *param)
{
	int item;
	while (true)
	{
		usleep((1 + rand() % 5) * 100000);
		item = 1000 + rand() % 1000;
		insert_item(item);
	}
}

void	*consumer(void *param)
{
	int item;
	while (true)
	{
		usleep((1 + rand() % 5) * 100000);
		remove_item(&item);
	}
}

int	main(int argc, char *argv[])
{
	int	i, numPro = 4, numCon = 4;
	pthread_t	tid;

	pthread_mutex_init(&mutex, NULL);
	sem_init(&empty, 0, BUFFER_SIZE);
	sem_init(&full, 0, 0);
	srand(time(0));
	//producers
	for (i = 0; i < numPro; i++)
		pthread_create(&tid, NULL, producer, NULL);
	for (i = 0; i < numCon; i++)
		pthread_create(&tid, NULL, consumer, NULL);
	sleep(3);
	return 0;
}
