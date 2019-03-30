[Python3 实例](/src/lesson25.examples/examples.md)
### Python 字符串大小写转换

以下代码演示了如何将字符串转换为大写字母，或者将字符串转为小写字母等：
```python
str = "www.github.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 
```
执行以上代码输出结果为：
```
WWW.GITHUB.COM
www.github.com
Www.github.com
Www.Github.Com
```
---
[Python3 实例](/src/lesson25.examples/examples.md)