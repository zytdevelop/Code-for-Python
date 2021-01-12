import time
import random as rd
num_list = [rd.random() for i in range(0, 200000)]

# 测试列表的sort()函数与内置函数sorted()的效率
sort_total_time = 0
sorted_total_time = 0
test_count = 1000
for i in range(0, test_count):
    start = time.time()
    num_list.sort()
    end = time.time()
    sort_time = end-start
    sort_total_time += sort_time

    start = time.time()
    new_list = sorted(num_list)
    end = time.time()
    sorted_time = (end-start)
    sorted_total_time += sorted_time


print('==============')
print('sort() 函数所用时间为 %d', (sort_total_time / test_count))
print('==============')

print('==============')
print('sorted() 函数所用时间为 %d', (sorted_total_time / test_count))
print('==============')