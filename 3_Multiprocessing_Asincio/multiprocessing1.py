from multiprocessing import Pool
import time
import os

def f(x):
    return x**x
if __name__ == '__main__':
    # cpu = os.cpu_count()
    # print(cpu)
    # with Pool(cpu) as p:
    #     starter_at = time.time()
    #     print(p.map(f, range(1,1000)))
    #     print(f"Time {time.time()-starter_at}")
    starter_at = time.time()
    for i in range(1,1000):
        print(f(i))
    print(f"Time {time.time() - starter_at}")
Pro