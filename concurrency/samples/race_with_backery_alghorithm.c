#include <pthread.h>
#include <stdio.h>

#define NUM_THREADS 2

int x = 5;
int choosing[NUM_THREADS] = {0}; // Choosed thread
int ticket[NUM_THREADS] = {0}; // Ticket number



void lock(int thread_id){
    choosing[thread_id] = 1;
    int max_ticket = 0;

    // maximum ticket value
    for (int i=0; i<NUM_THREADS; i++){
        if (ticket[i] > max_ticket){
            max_ticket = ticket[i];
        }
    }

    ticket[thread_id] = max_ticket + 1;
    choosing[thread_id] = 0;

    // Wait for other threads to finish their ticket selection and turn
    for (int i = 0; i < NUM_THREADS; i++) {
        if (i == thread_id) continue; // Skip the current thread

        while (choosing[i]); // Wait until thread i finishes choosing

        while (ticket[i] != 0 && (ticket[i] < ticket[thread_id] || 
               (ticket[i] == ticket[thread_id] && i < thread_id)));
    }
}

void unlock(int thread_id){
    ticket[thread_id] = 0; // release
}

void* increment(void* arg) {
    int thread_id = *(int*)arg;
    lock(thread_id);

    // Critical section 
    x++;

    unlock(thread_id);
    return NULL;
}

void* decrement(void* arg) {
    int thread_id = *(int*)arg;
    lock(thread_id);

    // Critical section
    x--;

    unlock(thread_id);
    return NULL;
}

int main() {
    pthread_t tid1, tid2;
    int threads_ids[NUM_THREADS] = {0, 1};

    for(int i = 0; i < 10; i++)
    {
        // Create threads
        pthread_create(&tid1, NULL, increment, &threads_ids[0]);
        pthread_create(&tid2, NULL, decrement, &threads_ids[1]);

        // Wait for threads to complete
        pthread_join(tid1, NULL);
        pthread_join(tid2, NULL);

        // Print the final value of x
        printf("Final value of x: %d\n", x);
    }


    return 0;
}
