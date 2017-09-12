
from sys import argv

script, input_file = argv

class weather_checking:
    def __init__(self):
        self.dict_in = {} #dict for info from weather_info.txt
        self.dict_out = {} #dict for search record and output for history()
        self.isfinished = False

    # import data from txt to dict in Chinese
    def data_import(self):
        with open(input_file, encoding = 'utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                if not len(line):
                    continue
                self.dict_in[line.split(',')[0]] = line.split(',')[1]

    def check(self):
        input_str = input("请输入城市名或者指令:")
        # check whether the city input is in the dict or not, if yes, print
        if input_str in self.dict_in.keys():
            record = self.dict_in[input_str]
            print (record)
            #save the search record into a record dict
            self.dict_out[input_str] = record
        # use "help" or "h" to trigger the help info.
        elif input_str == "help" or input_str == "h":
            print ("""
            输入城市名，查询该城市的天气；
            输入help，获取帮助文档；
            输入history，获取查询历史；
            输入quit，退出天气查询系统。
            """)
        # use "quit" or "exit" to exit
        elif input_str == "quit" or input_str == "exit":
            for key in self.dict_out.keys():
                print(key, self.dict_out[key])
            print("感谢使用，下次再见")
            self.isfinished = True
        # use "history" to pull the history record from record dict
        elif input_str == "history":
            for key in self.dict_out.keys():
                print(key, self.dict_out[key])
        else:
            print("输入错误")


play = weather_checking()
print ("""
输入城市名，查询该城市的天气；
输入help或者h，获取帮助文档；
输入history，获取查询历史；
输入quit或者exit，退出天气查询系统。
""")

while play.isfinished == False:
    play.data_import()
    play.check()
