#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#include <time.h>
#include <stdlib.h>

#include <semaphore.h>

#define MAX_USERS_IN_LIVE 2

sem_t sem;


void* login_and_do() {
  // up();
  sem_wait(&sem);
  int r = rand() % 11;
  printf("logged in: sleeping for %d seconds\n", r);
  sleep(r);
  printf("lggging out\n");
  // down();
  sem_post(&sem);
  return NULL;
}

int main() {
  sem_init(&sem, 0, MAX_USERS_IN_LIVE);
  srand(time(NULL));   // Initialization, should only be called once.

  pthread_t* threads = malloc(sizeof(pthread_t) * 10);  // 10 threads

  for(int i = 0; i < 10; i++) {
    pthread_create(&threads[i], NULL, login_and_do, NULL);
    // sleep(1);
  }

  for(int i = 0; i < 10; i++)
  {
    pthread_join(threads[i], NULL);
  }
  printf("Finished!\n");

  sem_destroy(&sem);

  return 0;
}