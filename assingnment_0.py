import os

def main():
    print(f"BEFORE FORKS ----------- PID = {os.getpid()} ---------- PPID = {os.getppid()} \n\n")

    os.fork()
    print(f"AFTER 1 FORK ----------- PID = {os.getpid()} ---------- PPID = {os.getppid()}")

    os.fork()
    print(f"AFTER 2 FORK ----------- PID = {os.getpid()} ---------- PPID = {os.getppid()}")

    os.fork()
    print(f"AFTER 3 FORK ----------- PID = {os.getpid()} ---------- PPID = {os.getppid()}")


if __name__ == "__main__":
    main()
