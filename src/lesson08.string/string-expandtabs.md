**[字符串](/src/lesson08.string/string.md)**
#### 描述
expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。

#### 语法
expandtabs()方法语法：
```python
str.expandtabs(tabsize=8)
```
#### 参数
- tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数。
#### 返回值
该方法返回字符串中的 tab 符号('\t')转为空格后生成的新字符串。

#### 实例
以下实例展示了expandtabs()方法的实例：
```python
#!/usr/bin/python3

str = "this is\tstring example....wow!!!"

print ("原始字符串: " + str)
print ("替换 \\t 符号: " +  str.expandtabs())
print ("使用16个空格替换 \\t 符号: " +  str.expandtabs(16))
```
以上实例输出结果如下：
```
原始字符串: this is     string example....wow!!!
替换 \t 符号: this is string example....wow!!!
使用16个空格替换 \t 符号: this is         string example....wow!!!
```
---
**[字符串](/src/lesson08.string/string.md)**