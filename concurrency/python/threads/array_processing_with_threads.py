import threading


def sum_array(array: list):
    print(f"Sum of {array} -> {sum(array)}")
    return sum(array)


def main(array: list):
    first_part = array[0:(len(array)//2)]
    second_part = array[(len(array)//2):]

    thread1 = threading.Thread(target=sum_array, args=(first_part, ))
    thread1.start()

    thread2 = threading.Thread(target=sum_array, args=(second_part, ))
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    main(array)
