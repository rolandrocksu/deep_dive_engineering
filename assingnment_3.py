import os

def main():
    res = os.fork()

    if res == 0:
        os.execl("/bin/echo", "echo", "Hello from the child process")
    
    print("Parent process done")


if __name__ == "__main__":
    main()
