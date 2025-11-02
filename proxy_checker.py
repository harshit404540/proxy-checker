import requests
import threading
import queue

class Main:
    def __init__(self):
        self.queue = queue.Queue()

    def fetch(self):
        with open("proxies.txt","r")as f:
            proxies = f.read().split("\n")
            for proxy in proxies:
                self.queue.put(proxy)

    def checking_proxy(self):
        while not self.queue.empty():
            proxy = self.queue.get()
            try:
                response = requests.get("http://ipinfo.io/json",
                                        proxies={"http": proxy, "https": proxy},
                                        timeout=5)
                if response.status_code == 200:
                    print(f"\033[92m[+] {proxy}\033[0m")
                else:
                    print(f"\033[91m[-] {proxy}\033[0m")
            except:
                print(f"\033[91m[-] {proxy} \033[0m")
                continue

    def run(self):
        self.fetch()
        for _ in range(10):
            thread = threading.Thread(target=self.checking_proxy).start()

if __name__ == "__main__":
    app = Main()

    app.run()
