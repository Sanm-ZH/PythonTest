[Python3 实例](/src/lesson25.examples/examples.md)
### Python 获取昨天日期

以下代码通过导入 datetime 模块来获取昨天的日期：
```python
# 引入 datetime 模块
import datetime
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday
 
# 输出
print(getYesterday())
```
执行以上代码输出结果为：
```
2015-06-10
```
以上实例输出的意思为昨天的日期是 2015 年 6 月 10 日。

---
[Python3 实例](/src/lesson25.examples/examples.md)