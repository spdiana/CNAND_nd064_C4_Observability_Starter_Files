import time
import random
import threading

import requests

endpoints = ('endpoint_a', 'endpoint_b', 'endpoint_c', 'endpoint_d', 'not_found', 'error')


def run():
    while True:
        try:
            target = random.choice(endpoints)
            requests.get("http://backend:5000/%s" % target, timeout=1)
            requests.get("http://frontend:5001/%s" % target, timeout=1)
            requests.get("http://trial:5002/%s" % target, timeout=1)

        except:
            pass


if __name__ == '__main__':
    for _ in range(5):
        thread = threading.Thread(target=run)
        thread.setDaemon(True)
        thread.start()

    while True:
        time.sleep(1)
