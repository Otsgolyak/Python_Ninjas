import random
import string
import requests
import time
import multiprocessing
import threading
import random
import os

class timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None  # Возвращает что угодно, чтобы использовать следующим образом: Timer("Message") as value:

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start)
        print(self.message.format(elapsed_time))

def count(n):
     while n > 0:
         n -= 1


def img_downloader():
    while True:
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        rand_img = ''.join(random.choice(chars) for x in range(5))
        url = 'http://i.imgur.com/%s.png' % rand_img
        r = requests.get(url)
        if r.url != "http://i.imgur.com/removed.png":
            with open("photo/%s.jpg" % rand_img, "wb") as code:
                code.write(r.content)
                break


def multiplier(count):
    for i in range(count):
        img_downloader()
        print('Processed items [%d]' % os.getpid())


if __name__ == '__main__':
    # Процессы
    # with timer('Elapsed: {}s'):
    #     count = 5
    #     img_d = [
    #         multiprocessing.Process(target=multiplier, args=(count,))
    #         for i in range(4)
    #     ]
    #     for p in img_d:
    #         p.start()
    #
    #     time.sleep(2)
    #
    #     for p in img_d:
    #         p.join()

    # Потоки
    with timer('Elapsed: {}s'):
        count = 5
        img_d = [
            threading.Thread(target=multiplier, args=(count,))
            for i in range(4)
        ]
        for p in img_d:
            p.start()

        time.sleep(2)

        for p in img_d:
            p.join()
