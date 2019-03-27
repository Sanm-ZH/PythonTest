[Python3 实例](/src/lesson25.examples/examples.md)
### Python 输出指定范围内的素数

素数（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。

以下实例可以输出指定范围内的素数：

##### 实例
```python
#!/usr/bin/python3
 
# 输出指定范围内的素数
 
# take input from the user
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
 
for num in range(lower,upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
```
执行以上程序，输出结果为：
```
$ python3 test.py 
输入区间最小值: 1
输入区间最大值: 100
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```
---
[Python3 实例](/src/lesson25.examples/examples.md)
