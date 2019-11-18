#引用Python3中MyQR的库直接生成指定链接的二维码


from MyQR import myqr

#具体参数查看myqr官方文档'https://github.com/sylnsfar/qrcode#examples'

version, level, qr_name = myqr.run('https://github.com/zytdevelop',
                                  version = 1,
                                  level ='H',
                                  picture = None,
                                  colorized = False,
                                  contrast = 1.0,
                                  brightness = 1.0,
                                  save_name = None,
                                  save_dir = os_getcwd()
                                  )

'''
# help(myqr)
Positional parameter
   words: str

Optional parameters
   version: int, from 1 to 40
   level: str, just one of ('L','M','Q','H')
   picutre: str, a filename of a image
   colorized: bool
   constrast: float
   brightness: float
   save_name: str, the output filename like 'example.png'
   save_dir: str, the output directory
   
'''
