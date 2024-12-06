import os

def main():
    res = os.fork()

    if res == 0:
        os.execl("/bin/bash", "bash", "-c", "cat test.txt | grep test")
    
    print("Parent process done")


if __name__ == "__main__":
    main()
