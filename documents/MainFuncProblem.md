# 关于__main__函数的疑问
-------------------

## __main__函数的意义是什么？
```python 
    """
    __main__ 表示当前模块
    """
    if __name__ == '__main__':
```


> 示例代码
```python
# const.py
PI = 3.14

def main():
    print("PI:%2f",PI)
    
main()

# python const.py 
# 输出结果为 PI:3.14

# area.py
import const

def cal_round_area(radius):
    return PI*(radius)**2
    
def main():
    print(cal_round_area(2))
    
main()

# python area.py
# 输出结果为 
# PI:3.14 
# 12.56



```















## [1][if __name__ == '__main__' 如何正确理解?](https://www.zhihu.com/question/49136398)
