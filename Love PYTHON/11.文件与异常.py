"""
从文件中读取数据
2020.8.25
with语句适用于对资源进行访问的场合，不管使用过程中发生异常都会执行必要的’清理‘操作，释放资源。
比如文件使用后自动关闭，线程中锁的自动获取和释放等
with 语句的语法格式：
with context_expression [as target(s)]:
"""
# 读取整个文件
with open('practice.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 文件路径（当文件不在python目录文件下）
file_path = 'C:\code.txt'
with open(file_path,encoding='UTF-8') as file_op:
    essay = file_op.read()
    print(essay)