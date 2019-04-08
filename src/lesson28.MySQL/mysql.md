### Python MySQL - mysql-connector 驱动
MySQL 是最流行的关系型数据库管理系统，如果你不不熟悉 MySQL，可以阅读我们的 MySQL 教程。

使用 mysql-connector 来连接使用 MySQL， mysql-connector 是 MySQL 官方提供的驱动器。

我们可以使用 pip 命令来安装 mysql-connector：
```
python -m pip install mysql-connector
```
使用以下代码测试 mysql-connector 是否安装成功：
```python
# demo_mysql_test.py
import mysql.connector
```
执行以上代码，如果没有产生错误，表明安装成功。

---
#### 创建数据库连接
可以使用以下代码来连接数据库：
```python
# demo_mysql_test.py

import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="yourusername",    # 数据库用户名
  passwd="yourpassword"   # 数据库密码
)
 
print(mydb)
```
#### 创建数据库
创建数据库使用 "CREATE DATABASE" 语句，以下创建一个名为 runoob_db 的数据库：
```python
# demo_mysql_test.py
import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("CREATE DATABASE runoob_db")
```
创建数据库前我们也可以使用 "SHOW DATABASES" 语句来查看数据库是否存在：
```python
# demo_mysql_test.py
# 输出所有数据库列表：

import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SHOW DATABASES")
 
for x in mycursor:
  print(x)
```
或者我们可以直接连接数据库，如果数据库不存在，会输出错误信息：
```python
# demo_mysql_test.py
import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
```
