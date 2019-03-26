[Python3 实例](/src/lesson25.examples/examples.md)
### Python 二次方程
以下实例为通过用户输入数字，并计算二次方程：
```python
#### 实例
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0
 
# 导入 cmath(复杂数学运算) 模块
import cmath
 
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
 
# 计算
d = (b**2) - (4*a*c)
 
# 两种求解方式
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
 
print('结果为 {0} 和 {1}'.format(sol1,sol2))
```
执行以上代码输出结果为：
```
$ python test.py 
输入 a: 1
输入 b: 5
输入 c: 6
结果为 (-3+0j) 和 (-2+0j)
```
该实例中，我们使用了 cmath (complex math) 模块的 sqrt() 方法 来计算平方根。
---
[Python3 实例](/src/lesson25.examples/examples.md)