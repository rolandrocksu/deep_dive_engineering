import os

def main():
    res = os.fork()

    if res == 0:
        os.execl("/bin/ls", "ls")
    
    os.wait()

    print("Parent process done")


if __name__ == "__main__":
    main()
