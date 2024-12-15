#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// TODO 
void* print_message(void* arg) {
    int thread_id = *(int*)arg;
    printf("Thread %d is running!", thread_id);
    return NULL;
}

int main() {
    pthread_t threads[3];

    for (int i=1; i<4; i++){
        if (pthread_create(&threads[i], NULL, print_message, &i) != 0) {
            perror("Failed to create thread");
            return 1;
        }
    }

    for (int i=1; i<4; i++){
        if (pthread_join(threads[i], NULL) != 0) {
            perror("Failed to join thread");
            return 1;
        }
    }

    return 0;
}