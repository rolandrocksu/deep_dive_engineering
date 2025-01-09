#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>
#define NUM_ITERATIONS 1000000


#define SLOTS 2


sem_t empthy;
sem_t full;


void *enter_parking(void *arg) {
    // up();
    sem_wait(&full);
    // down();
    sem_post(&empthy);

    int r = rand() % 11;
    printf("Parcking for %d seconds\n", r);
    sleep(r);
    return NULL;
}

void *living_parcking(void *args) {
    // up();
    sem_wait(&empthy);
    // down();
    sem_post(&full);

    int r = rand() % 11;
    printf("Going out -- \n");
    return NULL;
}


int main() {
    sem_init(&empthy, SLOTS, 0);
    sem_init(&full, 0, SLOTS);

    pthread_t* threads = malloc(sizeof(pthread_t) * 10);  // 10 threads

    for(int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, enter_parking, NULL);
        // sleep(1);
    }

    for(int i = 6; i < 10; i++) {
        pthread_create(&threads[i], NULL, living_parcking, NULL);
        // sleep(1);
    }

    for(int i = 0; i < 10; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Finished \n",);

    sem_destroy(&empthy);
    sem_destroy(&full);
    return 0;
}
