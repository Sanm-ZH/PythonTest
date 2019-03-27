x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))

x1 = input('输入 x 值: ')
y1 = input('输入 y 值: ')

# 不使用临时变量
x1, y1 = y1, x1

print('交换后 x 的值为: {}'.format(x1))
print('交换后 y 的值为: {}'.format(y1))