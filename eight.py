import time


def job(t):
    print("Start Job", t)
    time.sleep(t)
    print("Job", t, "takes", t, "s")


def main():
    [job(t) for t in range(1, 4)]


t1 = time.time()
main()
print("No async total time:", time.time() - t1)
