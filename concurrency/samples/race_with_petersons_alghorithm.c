#include <pthread.h>
#include <stdio.h>

int x = 5;
int favored;
int T1_Wants_To_Enter = 0;
int T2_Wants_To_Enter = 0;

void* increment(void* arg) {
    int T1_Wants_To_Enter = 1;
    favored = 2;

    while(T2_Wants_To_Enter == 1 && favored == 2){

    };

    x++;

    T1_Wants_To_Enter = 0;
    return NULL;
}

void* decrement(void* arg) {
    T2_Wants_To_Enter = 1;
    favored = 1;
    
    while(T1_Wants_To_Enter == 1 && favored == 1){

    };

    x--;

    T2_Wants_To_Enter = 0;
    return NULL;
}

int main() {
    pthread_t tid1, tid2;

    for(int i = 0; i < 10; i++)
    {
        // Create threads
        pthread_create(&tid1, NULL, increment, NULL);
        pthread_create(&tid2, NULL, decrement, NULL);

        // Wait for threads to complete
        pthread_join(tid1, NULL);
        pthread_join(tid2, NULL);

        // Print the final value of x
        printf("Final value of x: %d\n", x);
    }


    return 0;
}
