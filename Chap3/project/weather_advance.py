import xlrd
import requests
import json

KEY = '2l92mhanmczwzyov'
UID = "UCA7752FDD"
API = 'https://api.seniverse.com/v3/weather/now.json'
UNIT = 'c'
LANGUAGE = 'zh-Hans'

class WeatherChecker(object):
    def __init__(self):
        self.list_in = []  #dict for info from weather_info.txt
        self.dict_out = {}  #dict for search record and output for history()
        self.isfinished = False
        self.input_str = ''

    def data_import(self):
        data = xlrd.open_workbook('cities.xls')
        table = data.sheet_by_name(u'城市')
        for i in range(1, table.nrows):
            data_row = table.cell(i, 1).value
            self.list_in.append(data_row)

    def city_check(self):
        result = requests.get(
            API,
            params={
                'key':KEY,
                'location':self.input_str,
                'language':LANGUAGE,
                'unit':UNIT
            },
            timeout=1)
        decode = json.loads(result.text)
        record = [
            decode['results'][0]['now']['text'],
            decode['results'][0]['now']['temperature'],
            decode['results'][0]['now']['humidity'],
            decode['results'][0]['now']['wind_direction'],
            decode['results'][0]['last_update']
        ]
        return self.input_str + '\n'"天气:"+record[0] + '\n'"温度:"+record[1]+'\n'"相对湿度:"+record[2] \
            + '\n'"风向:"+record[3]+'\n'"更新时间:"+record[4]+'\n'

    def help_check(self):
        output = """
        输入城市名，查询该城市的天气；
        输入help，获取帮助文档；
        输入history，获取查询历史。
        """
        return output

    def exit_check(self):
        output = ''
        for key in self.dict_out.keys():
            output = output + key + self.dict_out[key]
            return output
        return "感谢使用，下次再见"
        self.isfinished = True

    def history_check(self):
        output = ''
        for key in self.dict_out.keys():
            output = output + self.dict_out[key]
        return output

    def check(self):
        #self.input_str = input("请输入城市名或者指令:")
        if self.input_str in self.list_in:
            output = self.city_check()
            self.dict_out[self.input_str] = output

        elif self.input_str == "help" or self.input_str == "h":
            output = self.help_check()

        elif self.input_str == "quit" or self.input_str == "exit":
            output = self.exit_check()

        elif self.input_str == "history":
            output = self.history_check()
        else:
            output = "输入错误"
        return output

if __name__ == '__main__':
    play = WeatherChecker()
    while play.isfinished == False:
        play.data_import()
        play.check()
