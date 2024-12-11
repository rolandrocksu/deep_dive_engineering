#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>


int main() {
    int res;
    res = fork();
    if (res == 0) {
        execl("/bin/echo", "echo", "Hello from the child process");
    }

    wait(NULL);

    printf("Parent process done");

    return 0;
}
