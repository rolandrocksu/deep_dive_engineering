#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void* square_of_number(void* arg) {
    int number = *(int*)arg;
    int result = number*number;
    printf("Square of %d is %d!\n", number, result);
    
    return NULL;
}

int main() {
    pthread_t threads[3];
    int threads_ids[3];

    for (int i=0; i<10; i++){
        threads_ids[i] = i+1;
        if (pthread_create(&threads[i], NULL, square_of_number, &threads_ids[i]) != 0) {
            perror("Failed to create thread");
            return 1;
        }
    }

    for (int i=0; i<10; i++){
        if (pthread_join(threads[i], NULL) != 0) {
            perror("Failed to join thread");
            return 1;
        }
    }

    return 0;
}