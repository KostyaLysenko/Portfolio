

import concurrent.futures
import time
from math import factorial




def factor(number):

    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial
starter_at1 = time.time()
print(factor(1000))
print(f"Time cycle while {time.time() - starter_at1}")

if __name__=="__main__":
    starter_at2 = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(factor(1000))
a=time.time()-starter_at2
print(f"Time ThreadPoolExecutor {a}")

if __name__=="__main__":
    starter_at3 = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(factor(1000))
b=time.time()-starter_at3
print(f"Time ProcessPoolExecutor {b}")
if a<b:
    print(f"Best result is {a} in ThreadPoolExecutor")
if a>b:
    print(f"Best result is {b} in ProcessPoolExecutor")