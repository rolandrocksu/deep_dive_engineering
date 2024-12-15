#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>


int main() {
    int res;
    res = fork();
    if (res == 0) {
        execl("/bin/ls", "ls", NULL);
    }

    res = fork();
    if (res == 0) {
        execl("/bin/date", "date", NULL);
    }


    wait(NULL);

    wait(NULL);

    printf("Parent process done");

    return 0;
}
