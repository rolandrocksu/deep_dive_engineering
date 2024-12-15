#include <stdio.h>
#include <unistd.h>


int main() {
    printf("BEFORE FORKS ----------- PID = %d ---------- PPID = %d\n\n", getpid(), getppid());

    fork();
    printf("AFTER 1 FORK ----------- PID = %d ---------- PPID = %d\n", getpid(), getppid());

    fork();
    printf("AFTER 2 FORK ----------- PID = %d ---------- PPID = %d\n", getpid(), getppid());

    fork();
    printf("AFTER 3 FORK ----------- PID = %d ---------- PPID = %d\n", getpid(), getppid());

    return 0;
}