[Python3 实例](/src/lesson25.examples/examples.md)
Python 约瑟夫生者死者小游戏

30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？

##### 实例
```python
people={}
for x in range(1,31):
    people[x]=1
# print(people)
check=0
i=1
j=0
while i<=31:
    if i == 31:
        i=1
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i+=1
            continue
        else:
            check+=1
            if check == 9:
                people[i]=0
                check = 0
                print("{}号下船了".format(i))
                j+=1
            else:
                i+=1
                continue
```
执行以上实例，输出结果为：
```
9号下船了
18号下船了
27号下船了
6号下船了
16号下船了
26号下船了
7号下船了
19号下船了
30号下船了
12号下船了
24号下船了
8号下船了
22号下船了
5号下船了
23号下船了
```
---
[Python3 实例](/src/lesson25.examples/examples.md)
