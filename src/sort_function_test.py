import time
import random as rd
num_list = [rd.random() for i in range(0, 200000)]

# 测试列表的sort()函数与内置函数sorted()的效率
for i in range(0, 1000):
    start = time.time()
    num_list.sort()
    end = time.time()
    print('==============')
    print('sort() 函数所用时间为 %d', (end-start))
    sort_time = end-start
    print('==============')

    start = time.time()
    new_list = sorted(num_list)
    end = time.time()
    print('==============')
    sorted_time = (end-start)
    print('sorted() 函数所用时间为 %d', (end-start))
    print('==============')