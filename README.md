# 系统开发
## ToDo
### 温馨堂宾馆系统开发
文件目录管理
依次说明上面的架势中每个目录和文件的作用（当然，这个作用是我规定的，读者如果愿意，也可以根据自己的意愿来任意设计）：

handlers：我准备在这个文件夹中放前面所说的后端python程序，主要处理来自前端的请求，并且操作数据库。
methods：这里准备放一些函数或者类，比如用的最多的读写数据库的函数，这些函数被handlers里面的程序使用。
statics：这里准备放一些静态文件，比如图片，css和javascript文件等。
templates：这里放模板文件，都是以html为扩展名的，它们将直接面对用户。