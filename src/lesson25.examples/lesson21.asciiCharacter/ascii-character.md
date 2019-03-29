[Python3 实例](/src/lesson25.examples/examples.md)
### Python ASCII码与字符相互转换

以下代码用于实现ASCII码与字符相互转换：

##### 实例
```python
# 用户输入字符
c = input("请输入一个字符: ")
 
# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))
 
 
print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))
```
执行以上代码输出结果为：
```
python3 test.py 
请输入一个字符: a
请输入一个ASCII码: 101
a 的ASCII 码为 97
101  对应的字符为 e
```
---
[Python3 实例](/src/lesson25.examples/examples.md)