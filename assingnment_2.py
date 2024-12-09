import os

def main():
    res = os.fork()

    if res == 0:
        os.execl("/bin/ls", "ls")
    
    res = os.fork()

    if res == 0:
        os.execl("/bin/date", "date")
    
    os.wait()
    os.wait()

    print("Parent process done")



if __name__ == "__main__":
    main()
