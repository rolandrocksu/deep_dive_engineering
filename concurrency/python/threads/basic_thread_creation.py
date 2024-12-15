import threading 


def threading_function(thread_id):
    print(f"Thread {thread_id} is running!")


def main():
    threads = []

    for i in range(1, 4):
        thread = threading.Thread(target=threading_function, args=(i, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


    
if __name__ == "__main__":
    main()
