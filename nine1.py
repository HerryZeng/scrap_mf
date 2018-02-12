import asyncio
import time


async def job(t):
    print("Start Job", t)
    await asyncio.sleep(t)
    print("Job", t, "takes", t, "s")


async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1, 4)]
    await asyncio.wait(tasks)


t1 = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print("Async total time:", time.time() - t1)
