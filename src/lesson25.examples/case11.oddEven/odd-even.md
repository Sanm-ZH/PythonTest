[Python3 实例](/src/lesson25.examples/examples.md)
### Python 判断奇数偶数

以下实例用于判断一个数字是否为奇数或偶数：

##### 实例
```python
# Python 判断奇数偶数
# 如果是偶数除于 2 余数为 0
# 如果余数为 1 则为奇数
 
num = int(input("输入一个数字: "))
if (num % 2) == 0:
   print("{0} 是偶数".format(num))
else:
   print("{0} 是奇数".format(num))
``` 
我们也可以使用内嵌 if 语句来实现：

执行以上代码输出结果为：
```
输入一个数字: 3
3 是奇数
```
---
[Python3 实例](/src/lesson25.examples/examples.md)

---
#### 优化加入输入判断:
```python
while True:
    try:
        num=int(input('输入一个整数：')) #判断输入是否为整数
    except ValueError: #不是纯数字需要重新输入
        print("输入的不是整数！")
        continue
    if num%2==0:
        print('偶数')
    else:
        print('奇数')
    break
```
