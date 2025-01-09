#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>
#define NUM_ITERATIONS 1000000

pthread_mutex_t mutex;
pthread_spinlock_t spinlock;
sem_t sem;

volatile int counter = 0;// Function for incrementing the counter (Critical Section)

void *increment_counter(void *arg) {
    for (int i = 0; i < NUM_ITERATIONS; i++) {
        // Critical Section: Increment the shared counter
	// Use all 3 mechanisms to sync this section. Keep two of them commented out.
        // pthread_mutex_lock(&mutex);
	//sem_wait(&sem);
	pthread_spin_lock(&spinlock);
	counter++;
	
	pthread_spin_unlock(&spinlock);
	// sem_post(&sem);
	
	//pthread_mutex_unlock(&mutex);
    }
    return NULL;
}


int main() {
    // sem_init(&sem, 0, 1);

    pthread_spin_init(&spinlock, PTHREAD_PROCESS_PRIVATE);

    pthread_t thread1, thread2;    // Create two threads
    pthread_create(&thread1, NULL, increment_counter, NULL);
    pthread_create(&thread2, NULL, increment_counter, NULL);    // Wait for threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);    // Print the final value of the counter
    printf("Final Counter: %d\n", counter);

    pthread_spin_destroy(&spinlock);

    
    // sem_destroy(&sem);
    return 0;
}

