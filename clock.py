from time import strftime, sleep

def time():
    while True:
        string = strftime('%H:%M:%S %p')
        print(string, end="\r", flush=True)
        sleep(1)

if __name__ == "__main__":
    time()
