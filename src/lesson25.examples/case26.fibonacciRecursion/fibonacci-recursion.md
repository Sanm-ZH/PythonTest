[Python3 实例](/src/lesson25.examples/examples.md)
### Python 使用递归斐波那契数列

以下代码使用递归的方式来生成斐波那契数列：

##### 实例
```python
 
def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
 
# 获取用户输入
nterms = int(input("您要输出几项? "))
 
# 检查输入的数字是否正确
if nterms <= 0:
   print("输入正数")
else:
   print("斐波那契数列:")
   for i in range(nterms):
       print(recur_fibo(i))
```
执行以上代码输出结果为：
```
您要输出几项? 10
斐波那契数列:
0
1
1
2
3
5
8
13
21
34
```
---
[Python3 实例](/src/lesson25.examples/examples.md)