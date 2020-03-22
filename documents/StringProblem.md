# 关于Python中字符串操作的疑问
-------------


## 对于字符串对象的join()函数和 ' + ' 操作符号之间的性能差距

```python
# 使用 ' + ' 操作符直接连接字符串
    def str_join(num):
        str = 'hello'
        for i in range(num):
            str += 'x'
        return str

# 字符串转换为列表类型再使用join()方法进行拼接
    def str_join2(num):
        str = 'hello'
        str = list(str)
        for i in range(num):
            append('x')
        return ''.join(str)
```
### 实际运行结果参考文献
[1][Python字符串通过 '+' 和join()方法拼接字符串的性能差距](https://blog.csdn.net/Jerry_1126/article/details/86584936)


### 观察结果：字符串大小较小的情况下两种方法的性能接近；随着字符串增大，’+‘操作符直接连接的时间开销和内存开销不断增大。
### 原因：由于字符串为不可变对象，’+‘操作符直接连接字符串是不断进行创建新的字符串对象的过程，随着字符串数据的增大创建对象的开销也就增大了。
