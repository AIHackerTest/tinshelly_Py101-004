import xlrd
import requests
import json
from const_value import API, KEY, UNIT, LANGUAGE


class WeatherChecker:
    def __init__(self):
        self.list_in = [] #dict for info from weather_info.txt
        self.dict_out = {} #dict for search record and output for history()
        self.isfinished = False
        self.input_str = ''

    def data_import(self):
        data = xlrd.open_workbook('cities.xls')
        table = data.sheet_by_name(u'城市')
        for i in range(1, table.nrows):
            data_row = table.cell(i,1).value
            self.list_in.append(data_row)

    def city_check(self):
        result = requests.get(API, params={
            'key':KEY,
            'location':self.input_str,
            'language':LANGUAGE,
            'unit':UNIT
            }, timeout=1)
        decode = json.loads(result.text)
        record = [decode['results'][0]['now']['text'],
                  decode['results'][0]['now']['temperature'],
                  decode['results'][0]['now']['humidity'],
                  decode['results'][0]['now']['wind_direction'],
                  decode['results'][0]['last_update']]
        return '\n'"天气:"+record[0] + '\n'"温度:"+record[1]+'\n'"相对湿度:"+record[2] \
            + '\n'"风向:"+record[3]+'\n'"更新时间:"+record[4]+'\n'

    def help_check(self):
        print ("""
        输入城市名，查询该城市的天气；
        输入help，获取帮助文档；
        输入history，获取查询历史；
        输入quit，退出天气查询系统。
        """)

    def exit_check(self):
        for key in self.dict_out.keys():
            print(key, self.dict_out[key])
        print("感谢使用，下次再见")
        self.isfinished = True

    def history_check(self):
        for key in self.dict_out.keys():
            print(key,self.dict_out[key])

    def check(self):
        self.input_str = input("请输入城市名或者指令:")
        if self.input_str in self.list_in:
            print(self.city_check())
            self.dict_out[self.input_str] = self.city_check()

        elif self.input_str == "help" or self.input_str == "h":
            self.help_check()

        elif self.input_str == "quit" or self.input_str == "exit":
            self.exit_check()

        elif self.input_str == "history":
            self.history_check()
        else:
            print("输入错误")


play = WeatherChecker()
print ("""
输入城市名，查询该城市的天气；
输入help或者h，获取帮助文档；
输入history，获取查询历史；
输入quit或者exit，退出天气查询系统。
""")
while play.isfinished == False:
    play.data_import()
    play.check()
