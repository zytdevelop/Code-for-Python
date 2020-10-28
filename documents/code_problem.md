# 编码问题
对于英文而言  
 - str: 'hello'  
    + 内存中的表现形式: Unicode  
    + 文件中的表现形式: 'hello'  
- bytes:
    + 内存中的表现形式: 非Unicode
    + 文件中的表现形式: b'hello'
    
对于中文而言  
 - str: '汉字'  
    + 内存中的表现形式: Unicode  
    + 文件中的表现形式: '汉字'  
- bytes:
    + 内存中的表现形式: 非Unicode(python3x中为UTF-8)
    + 文件中的表现形式: b'\xe6\xb1\x89\xe5\xad\x97'
    
 - python3x 中的编码函数encode(), 解码函数为decode()
 