# 变量和基本结构
x = 1  # assign variable x the value 1
y = x + 5  # assign variable y the value of x plus 5
z = y  # assign variable z the value of y
print(x, y, z)

# 使用数子
x = 1  # integer
x = 1.0  # decimal (floating point)
print(x, y, z)

# type() 数据类型
x = 1
print(type(x))  # outputs: <class 'int'>

x = 1.0
print(type(x))  # outputs: <class 'float'>

# bool 类型
x = True
print(type(x))  # outputs: <class 'bool'>

# 字符串
x = 'This is a string'
print(x)  # outputs: This is a string
print(type(x))  # outputs: <class 'str'>
y = "This is also a string"
print(x)

# 对代码进行注释
# I am a comment...
x = 1  # the rest of the line is a comment
# ... and this is a 3rd comment
text = "# But this isn't a comment because it's a string literal and in quotes."

# This is a comment
# that crosses multiple lines

# 读取键盘输入
name = input('enter your name:')
print(name)

# input 函数始终返回键入值为字符串
x = input('Enter a number: ')
print(type(x))

# 若要讲值转换为整数变量，可以使用int函数
x = int(input('Enter a number: '))
print(type(x))

# 将数字转换为字符串
x = 5
print('The number is ' + str(x))