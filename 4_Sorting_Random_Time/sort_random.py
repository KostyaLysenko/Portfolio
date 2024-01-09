import random, time

from random_words import RandomWords

int_list=[]
float_list=[]
str_list=[]
w=RandomWords()

for i in range(0,5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

print("Int list", int_list)
print("Float list", float_list)
print("String list", str_list)

def bubble_sort(data):
    cor_time = time.time()
    lenght=len(data)
    count=0
    for iIndex in range(lenght):
        count+=1
        swapped = False
        for jIndex in range(0, lenght-iIndex-1):
            if data[jIndex]>data[jIndex+1]:
                data[jIndex],data[jIndex+1]=data[jIndex+1],data[jIndex]
                swapped=True
        if not swapped:
            break
    print("Sorted data", data)
    print("Count iterations", count)
    last_time= time.time() - cor_time
    print("Duration time", last_time)
    print(f"Середній час робооти алгоритму сортування на одну ітерацію: {last_time/count}")
bubble_sort(int_list)
# print("*"*50)
bubble_sort(float_list)
# print("*"*50)
bubble_sort(str_list)