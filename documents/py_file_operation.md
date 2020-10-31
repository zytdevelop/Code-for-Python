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


## 修改
思路:
1. 读模式打开原文件作为fp1
2. 写模式创建一个新文件fp2
3. 将 fp1 修改完毕, 写入fp2
4. 删除 fp1, 将 fp2 重命名为 fp1

```python
import os
with open('fp1.txt', encoding='utf-8') as fp1, open('fp2.txt', encoding='uft-8', mode='w') as fp2:
    source_data = fp1.read()
    # 中间修改原文件的内容
    fp2.write()
os.remove('fp1.txt')
os.rename('fp2.txt', 'fp1.txt')

```