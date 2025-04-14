import asyncio
from datetime import datetime
import random
import threading
import aiohttp
import requests

from timeing import count_time

def download_file_and_save(file_url):
    response = requests.get(file_url, allow_redirects=True)
    if response.status_code == 200:
        with open(f"test_data/{random.randint(1, 10**10)}.png", "wb") as f:
            f.write(response.content)
    else:
        print("SMTH WRONG!!!")

@count_time
def download_file_synchron(file_url, times):
    for _ in range(times):
        download_file_and_save(file_url)

@count_time
def download_file_with_threads(file_url, times):
    threads_list = []
    for _ in range(times):
        t = threading.Thread(target=download_file_and_save, args=(file_url, ))
        t.start()
        threads_list.append(t)

    for th in threads_list:
         th.join()

async def download_file_with_async(file_url, times):
    for _ in range(times):
        async with aiohttp.ClientSession() as session:
            async with session.get(file_url) as resp:
                if resp.status == 200:
                    with open(f"test_data/{random.randint(1, 10**10)}.png", "wb") as f:
                        result = resp.content.read()
                        f.write(result)


def main():
    file_url = "https://loremflickr.com/1000/1000"
    times = 20

    # run sequential
    # download_file_synchron(file_url, times)

    # run multithreads
    # download_file_with_threads(file_url, times)

    # run async
    now = datetime.now()
    asyncio.run(download_file_with_async(file_url, times))
    then = datetime.now()
    time_count = then - now 
    print(f"time_taked ---> {time_count.seconds}")
    

if __name__ == "__main__":
    main()