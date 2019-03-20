**[字符串](/src/lesson08.string/string.md)**
#### 描述
decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。

#### 语法
decode()方法语法：
```python
bytes.decode(encoding="utf-8", errors="strict")
```
#### 参数
- encoding -- 要使用的编码，如"UTF-8"。
- errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
#### 返回值
该方法返回解码后的字符串。

#### 实例
以下实例展示了decode()方法的实例：
```python
#!/usr/bin/python3
 
str = "弓长三郎";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
 
print(str)
 
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
```
以上实例输出结果如下：
```
弓长三郎
UTF-8 编码： b'\xe5\xbc\x93\xe9\x95\xbf\xe4\xb8\x89\xe9\x83\x8e'
GBK 编码： b'\xb9\xad\xb3\xa4\xc8\xfd\xc0\xc9'
UTF-8 解码： 弓长三郎
GBK 解码： 弓长三郎
```
---
**[字符串](/src/lesson08.string/string.md)**