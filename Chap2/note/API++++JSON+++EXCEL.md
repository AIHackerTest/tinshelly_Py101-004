
# API调用 - 使用 requests
## 1. 安装Requests模块

   $Python3 –m pip install requests
   
   result = requests.get(url, params, timeout)
       url = API提供的接口地址
       params = 相关参数设置，如密码，语言，气温单位等
       timeout = 1


```python
#心知天气API

import requests

KEY = '4r9bergjetiv1tsd'  # API key
UID = "U785B76FC9"  # 用户ID

LOCATION = 'beijing'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言
result = requests.get(API, params={
     'key': KEY,
     'location': LOCATION,
     'language': LANGUAGE,
     'unit': UNIT
}, timeout=1)
print(result.text)
```

    {"results":[{"location":{"id":"WX4FBXXFKE4F","name":"北京","country":"CN","path":"北京,北京,中国","timezone":"Asia/Shanghai","timezone_offset":"+08:00"},"now":{"text":"晴","code":"0","temperature":"31","feels_like":"29","pressure":"1008","humidity":"19","visibility":"31.1","wind_direction":"西","wind_direction_degree":"290","wind_speed":"16.2","wind_scale":"3","clouds":"","dew_point":""},"last_update":"2017-08-25T12:05:00+08:00"}]}
    

## 2. JSON()

   json.dumps 将 Python 对象编码成 JSON 字符串
   
   json.loads 将已编码的 JSON 字符串解码为 Python 对象


```python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print(json)
```

    [{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}]
    


```python
#使用参数让 JSON 数据格式化输出
import json
print (json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': ')))
```

    {
        "a": "Runoob",
        "b": 7
    }
    


```python
import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print (text)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    

# 读取excel
    
* 安装xlrd模块
    
  $Python3 –m pip install requests
  

* 打开Excel文件读取数据

  data = xlrd.open_workbook('excel.xls')
  
* 获取一个工作表

  table = data.sheets()[0]       #通过索引顺序获取
  
  table = data.sheet_by_index(0) #通过索引顺序获取
  
  table = data.sheet_by_name(u'Sheet1')#通过名称获取

* 获取整行和整列的值（返回数组）

  table.row_values(i)
  
  table.col_values(i)
  
* 获取行数和列数

  table.nrows
  
  table.ncols

* 获取单元格

  table.cell(0,0).value
  
  table.cell(2,3).value
