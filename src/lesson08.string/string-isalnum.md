**[字符串](/src/lesson08.string/string.md)**
#### 描述
isalnum() 方法检测字符串是否由字母和数字组成。

#### 语法
isalnum()方法语法：
```python
str.isalnum()
```
#### 参数
无。
#### 返回值
如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

#### 实例
以下实例展示了isalnum()方法的实例：
```python
#!/usr/bin/python3
 
str = "sanm-zh 2019"  # 字符串没有空格
print (str.isalnum())
 
str = "github.com/sanm-zh"
print (str.isalnum())
```
以上实例输出结果如下：
```
False
False
```
---
**[字符串](/src/lesson08.string/string.md)**