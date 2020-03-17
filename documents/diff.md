# python 2.x 和3.x区别

## 1. 版本说明

python2.6是python2.x和python3.x的过渡版本,python3.x设计的时候没有考虑向下兼容,  
导致大量python2.x的程序没有办法在python3.x环境上执行
  
   
## 2. print

- 在python2.x中print包含3种用法: 
```python
  print "string"    # print作为语句的用法
  print ("string")    # print作为函数的用法
  print("string")
```
  
- python3.x只有后面两种用法

## 3. 类型比较
- python2.x 比较不同的类型会返回False  
- python3.x 比较不同类型会抛出异常
  
## 4. 字符串编码类型
- python2.x 字符串编码类型为 ``` ASCII码 ```
- python3.x 字符串编码类型为 ``` utf-8 ```
  
## 5. 输入函数
- python2.x 输入函数有两个
```python
  text1 = input("Enter text: ")
  text2 = raw_input("Enter text: ")
```
  
- python3.x 删除了raw_input()函数,只剩下input()函数
  
## 6.赋值变量,扩展的可迭代解包
```python
  a, b, *res = [1, 2, 3, 4]    # 在 python2.x 中报错,但是在python3.x中不是合法的
```
  
## 7. 异常处理
- 异常的继承
  - python2.x 所有类型对象的异常都抛出  
  - python3.x 只有继承自BaseException类的对象才会被抛出,更加严格规范
- 异常的语法
  - python2.x 中下面语法是正确
  ```python
      try:
          10/0
      except Exception,e:
          print 'error',e
  ```
  - 在python3.x 中上述语法报错,必须使用 ```as```关键字
  ```python
      try:
          10/0
      except Exception as e:
          print('error',e)
  ```
- 异常的捕获
  - python2.x 捕获异常可以直接用逗号隔开异常和参数
  ```python
      try:
          10/0
      except Exception,e:
          raise Exception,e
  ```
  - python3.x 捕获异常必须用括号来匹配异常和args
    ```python
      try:
          10/0
      except Exception as e:
          raise Exception(e)
  ```
  
## 8. 字典
- python3.x 删掉了 python2.x中的iterkey()
- python3.x 用 ```in``` 关键字替代了python2.x 中的has_key()
- python3.x 的字典里面```dict.keys(), dict.items(), dict.values()``` 返回迭代器
  
## 9.
