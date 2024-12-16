#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void* print_numbers(void* arg) {
    int thread_id = *(int*)arg;
    for (int i=0; i<=5; i++){
        printf("THREAD_ID = %d | NUMBER  = %d \n", thread_id, i);
    }
    
    return NULL;
}

int main() {
    pthread_t threads[3];
    int threads_ids[3];

    for (int i=0; i<3; i++){
        threads_ids[i] = i+1;
        if (pthread_create(&threads[i], NULL, print_numbers, &threads_ids[i]) != 0) {
            perror("Failed to create thread");
            return 1;
        }
    }

    for (int i=0; i<3; i++){
        if (pthread_join(threads[i], NULL) != 0) {
            perror("Failed to join thread");
            return 1;
        }
    }

    return 0;
}