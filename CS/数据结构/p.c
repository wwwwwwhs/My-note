
#include <stdio.h>
#include <pthread.h>//线程 wait,post
#include <semaphore.h>
#include <unistd.h>
#include <string.h> // 放产品，字符串
#include <time.h>
#include <stdlib.h>

#define BUF_SIZE_MAX 256 //用于存放产品，可以存放字符串，字符串的长度上限

char* pBuffer;//临界资源

sem_t mutex;//互斥量，用于给缓冲区加锁，一般初值为1
sem_t full;//同步信号量，表示产品的数量，占用缓冲区的数量，初始值0
sem_t empty;//同步信号量，表示缓冲区空闲空间数量，初始值1

void* producer();//声明生产者线程函数
void* consumer();//声明消费者线程函数

/*
* 经典问题：
* 生产者和消费者问题
*/
int main()
{
	pBuffer = (char*)malloc(BUF_SIZE_MAX);//申请一个缓冲区空间
	
	pthread_t m_produce;//生产者线程信息
	pthread_t m_consume;//消费者线程信息
	
	sem_init(&mutex,0,1);//互斥量初始值1
	sem_init(&full,0,0);//同步信号量,产品数量初始值0
	sem_init(&empty,0,1);//同步信号量，缓冲区空闲数量初始值1
	
	pthread_create(&m_produce,NULL, producer, NULL);//生产者线程
	pthread_create(&m_consume,NULL, consumer, NULL);//消费者线程

	pthread_join(m_produce,NULL);//等待生产者线程退出
	pthread_join(m_consume,NULL);//等待消费者线程退出

   	sem_destroy(&full);//释放资源
   	sem_destroy(&empty);
   	sem_destroy(&mutex);

	free(pBuffer);//释放缓冲区
	
	printf("结束\n");

	return 0;
}

/*
* 生产者函数
* 功能：判断缓冲区是否空闲，如果缓冲区不满，则放入产品
* 处理：先判断P empty，再加锁P mutex，然后放产品，释放锁V mutex，同步信号量V full
*/
void* producer()
{
	printf("生产者线程\n");
	while(1)
	{
		sleep(1);

		sem_wait(&empty);//P操作-1,判断缓冲区是否为空
		sem_wait(&mutex);//P操作-1,对缓冲区枷锁
		
		snprintf(pBuffer, BUF_SIZE_MAX, "%d个苹果", rand()%10+1);
		printf("生产者放入:%s\n", pBuffer);
		
		sem_post(&mutex);//V操作+1，释放锁
		sem_post(&full);//V操作+1,同步给消费者
	}
}

/*
* 消费者函数
* 功能：判断缓冲区是否有产品，如果有数据，则取出产品
* 处理：先判断P full，再加锁P mutex，然后取产品，释放锁V mutex，同步信号量V empty
*/
void* consumer()
{
	printf("消费者线程\n");
	while(1)
	{
		sleep(1);

		sem_wait(&full);//P操作-1,判断缓冲区是否有产品
		sem_wait(&mutex);//P操作-1,对缓冲区枷锁
		
		printf("消费者取出:%s\n\n", pBuffer);
		memset(pBuffer, 0, BUF_SIZE_MAX);//清空缓冲区
		
		sem_post(&mutex);//V操作+1,释放锁
		sem_post(&empty);//V操作+1,同步给生产者
	}
}


