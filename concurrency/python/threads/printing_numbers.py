import threading

def print_numbers(thread_id: int):
    for i in range(100):
        print(f"THREAD_ID = {thread_id} | NUMBER  = {i}")


def main():

    threads = []

    for i in range(1, 10):
        thread = threading.Thread(target=print_numbers, args=(i, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
 