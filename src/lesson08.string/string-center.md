**[字符串](/src/lesson08.string/string.md)**
#### 描述
center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
#### 语法
center()方法语法：
```
str.center(width[, fillchar])
```
#### 参数
- width -- 字符串的总宽度。
- fillchar -- 填充字符。
#### 返回值
返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。

#### 实例
以下实例展示了center()方法的实例：
```python
#!/usr/bin/python3

str = "[Sanm-ZH]"

print ("str.center(40, '*') : ", str.center(40, '*'))
```
以上实例输出结果如下：
```
str.center(40, '*') :  ***************[Sanm-ZH]****************
```
---
**[字符串](/src/lesson08.string/string.md)**