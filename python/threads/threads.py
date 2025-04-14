import requests
import threading

from timeing import count_time



def feth_content(url: str):
    req = requests.get(url)
    print(req.status_code, url)

@count_time
def feth_contents_with_threading(urls: list):
    threads_list = []

    for url in urls:
        thread = threading.Thread(target=feth_content, args=(url, ))
        thread.start()
        threads_list.append(thread)

    for thread in threads_list:
        thread.join()

@count_time
def feth_contents_without_threading(urls: list):
    for url in urls:
        feth_content(url)


if __name__ == "__main__":
    urls = [
        "http://www.youtube.com",
        "http://www.facebook.com",
        "http://www.baidu.com",
        "http://www.yahoo.com",
        "http://www.amazon.com",
        "http://www.wikipedia.org",
        "http://www.qq.com",
        "http://www.google.co.in",
        "http://www.twitter.com",
        "http://www.live.com",
        "http://www.taobao.com",
        "http://www.bing.com",
        "http://www.instagram.com",
        "http://www.weibo.com",
        "http://www.sina.com.cn",
        "http://www.linkedin.com",
        "http://www.yahoo.co.jp",
        "http://www.msn.com",
        "http://www.vk.com",
        "http://www.google.de",
        "http://www.yandex.ru",
    ]

    feth_contents_with_threading(urls)
    feth_contents_without_threading(urls)
