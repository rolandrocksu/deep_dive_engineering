#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void* print_message(void* arg) {
    int thread_id = *(int*)arg;
    printf("Thread %d is running! \n", thread_id);
    return NULL;
}

int main() {
    pthread_t threads[3];
    int threads_ids[3];

    for (int i=0; i<3; i++){
        threads_ids[i] = i+1;
        if (pthread_create(&threads[i], NULL, print_message, &threads_ids[i]) != 0) {
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
