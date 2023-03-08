//n개의 접근점을 관리할 수 있는 방법 (n으로 초기화 필요)
//Binary Semaphores (n = 1)은 Mutex Lock과 비슷하며, 여러 프로세스를 대응할 수 있다는 점이 다르다
//n > 1의 경우, 접근점이 같은 변수를 공유하는 경우 mutual exclusive가 지켜지지 않는다

#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>

int sum = 0;
sem_t sem;

void *counter(void *param)
{
	int i;
	for (i = 0; i < 100000; i++)
	{
		//entry
		sem_wait(&sem);
		
		//critical
		sum++;
		
		//exit
		sem_post(&sem);
		
		//remainder
	}
	pthread_exit(0);
}

int main()
{
	pthread_t tid[5];
	int i;
	sem_init(&sem, 0, 1);	//초기화할 sem, (0), n개수
	
	for (i = 0; i < 5; i++)
		pthread_create(&tid[i], NULL, counter, NULL);
	for (i = 0; i < 5; i++)
		pthread_join(tid[i], NULL);
	printf("%d\n", sum);
}
