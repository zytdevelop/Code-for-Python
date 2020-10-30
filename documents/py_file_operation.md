# python3.x 文件操作
## 打开文件
```python
# 第一种方法, 直接使用open(), 需要手动关闭文件
fp = open('/')
data = fp.read()
print(data)
fp.close()

# 第二种方法, 使用with 关键字, 不需要手动关闭文件
with open('/') as fp:
    data = fp.read()
    print(data)
```
- 打开文件操作可能存在的错误及原因:
    + UnicodeDecodeError:文件存储与文件打开时的编码集不一致
    + SyntaxError:文件路径参数内含有转义字符
## 读
- 四种模式: r, rb, r+, r+b
- rb: 操作非文本的文件--> 图片，视频，音频
- r: 
```python
with open('/') as fp:
    fp.read() # 返回整个文件
    fp.readlines() # 返回一个列表，列表每个元素是源文件的一行
    fp.readline() # 返回文件的一行内容
    

```

## 写
- 四种模式: w, wb, w+, w+b

## 追加
- 四种模式: a, ab, a+, a+b

## 其他功能
- tell() 返回光标位置
- seek() 跳转到文件指定位置