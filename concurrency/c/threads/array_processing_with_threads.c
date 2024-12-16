#include <stdio.h>
#include <pthread.h>

void* sum_array(void* arg) {
    int* array = (int*)arg;
    int size = array[0];
    int sum = 0;

    for  (i=0, i <= size, i++){
        sum += array[i];
    }



    printf("sum = %d \n", sum);
    return sum;
}


int main() {
    int array[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = sizeof(array) / sizeof(array[0]);
    int mid = size / 2;


    int first_part[mid + 1];
    int second_part[size - mid + 1];

    

}