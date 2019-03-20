**[字符串](/src/lesson08.string/string.md)**

#### 描述
find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

#### 语法
find()方法语法：
```
str.find(str, beg=0, end=len(string))
```
#### 参数
- str -- 指定检索的字符串
- beg -- 开始索引，默认为0。
- end -- 结束索引，默认为字符串的长度。
#### 返回值
如果包含子字符串返回开始的索引值，否则返回-1。

#### 实例
以下实例展示了find()方法的实例：
```python
#!/usr/bin/python3
 
str1 = "sanm-zh example....wow!!!"
str2 = "exam";
 
print (str1.find(str2))
print (str1.find(str2, 5))
print (str1.find(str2, 10))
```
以上实例输出结果如下：
```
8
8
-1
```
#### 实例
```
>>>info = 'abca'
>>> print(info.find('a'))      # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
0
>>> print(info.find('a', 1))   # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3
3
>>> print(info.find('3'))      # 查找不到返回-1
-1
>>>
```
---
**[字符串](/src/lesson08.string/string.md)**