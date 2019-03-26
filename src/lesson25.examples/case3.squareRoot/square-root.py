import  cmath

num = float(input('请输入一个数字：'))

num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num , num_sqrt))

num2 = int(input("请输入一个数字: "))
num_sqrt2 = cmath.sqrt(num2)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num2 ,num_sqrt2.real,num_sqrt2.imag))