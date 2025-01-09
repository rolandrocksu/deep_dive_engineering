#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

pthread_mutex_t mutex;
volatile int counter = 0;
volatile int previous = 0;

void *write_and_do_smth(void *arg) {

    while( 1 ){
        pthread_mutex_lock(&mutex);
        sleep(1);
        counter++;	
        pthread_mutex_unlock(&mutex);
    }

    return NULL;
}


void *read_and_do_smth(void *args) {
    while (1 ){
        int changed = counter - previous;
        int current_value = counter % 2;

        printf("Changed %d times \n", changed);
        printf("Current value == %d \n", current_value);

        sleep(5);

        int previous = counter;
    }
}


int main() {

    pthread_t thread1, thread2;    // Create two threads
    pthread_create(&thread1, NULL, write_and_do_smth, NULL);
    pthread_create(&thread2, NULL, read_and_do_smth, NULL);    // Wait for threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);    // Print the final value of the counter
    printf("Final Counter: %d\n", counter);

    return 0;
}
