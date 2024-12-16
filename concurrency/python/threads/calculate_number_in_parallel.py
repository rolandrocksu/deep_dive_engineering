import threading

def square_of_number(number: int):
    result = number**2
    print(f"Square of {number} is {result}!")
    return result


def main():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
    threads = []

    for num in numbers:
        thread = threading.Thread(target=square_of_number, args=(num, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
