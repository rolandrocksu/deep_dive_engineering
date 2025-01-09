#include <pthread.h>
#include <stdio.h>

#define NUM_THREADS 25

pthread_mutex_t mutex;

pthread_barrier_t barrier;
int zar_values[NUM_THREADS];



void* play_zar(void* arg) {
    while (1) {
        int* num = (int*)arg;
        int zar_value = rand() % 6;

        printf("Zar value = %d", zar_value);

        zar_values[num] = zar_value;

        pthread_barrier_wait(&barrier);
    }
    return NULL;
}

int main() {
    pthread_barrier_init(&barrier, NULL, NUM_THREADS);
    pthread_t threads[NUM_THREADS];

    for(int i = 0; i < NUM_THREADS; i++)
    {
        pthread_create(&threads[i], NULL, play_zar, &i);
        printf("Values ");
    }

    for(int i = 0; i < NUM_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }
    
    pthread_barrier_destroy(&barrier);



    return 0;
}
