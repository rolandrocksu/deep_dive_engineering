#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct {
    int *array;
    int start;
    int end;
} ThreadData;

void* sum_array(void* arg) {
    ThreadData* data = (ThreadData*)arg;

    int sum = 0;

    for  (int i=data->start; i <= data->end; i++){
        sum += data->array[i];
    }

    printf("Sum of array[%d:%d] = %d\n", data->start, data->end, sum);
    return NULL;
}


int main() {
    int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = sizeof(array) / sizeof(array[0]);
    int mid = size / 2;

    ThreadData data1 = {array, 0, mid-1};
    ThreadData data2 = {array, mid, size-1};

    pthread_t thread1, thread2;

    pthread_create(&thread1, NULL, sum_array, &data1);
    pthread_create(&thread2, NULL, sum_array, &data2);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("All processes completed.");

    return 0;

}
