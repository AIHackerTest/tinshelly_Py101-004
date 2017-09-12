import random

class random_game:
    def __init__(self, from_num, to_num, times):
        # 初始化随机数的范围，控制次数
        self.from_num = from_num
        self.to_num = to_num
        self.times = times
        self.num = random.randint(self.from_num, self.to_num)
        self.count_times = 0
        self.entered_num = 0
        self.isfinished = False

    # for debug
    def speak(self):
        print("generate a random number {} from {} to {}, current time is {}, finish when times = {} "
        .format(self.num, self.from_num, self.to_num, self.count_times, self.times))

    def input_num(self):
        # get the initial input
        input_str = input("Please enter a num between {} and {}：" .format(self.from_num, self.to_num))
        # start to check if input string is a number
        while input_str.isdigit() == False:
             print("{} is not a number" .format(input_str))
             input_str = input("Please enter a num between {} and {}：" .format(self.from_num, self.to_num))
        self.entered_num = int(input_str)
        self.count_times = self.count_times + 1
        print("You have entered a num: {}" .format(self.entered_num))

    def check(self):    
        if self.num == self.entered_num :
            self.isfinished = True
            print("Congratuations! You got the right number!")
        elif self.num > self.entered_num:
            print("Sorry! {} is Small!" .format(self.entered_num))
            if self.count_times >= self.times:
                self.isfinished = True
                print("Sorry! You have used all {} chances." .format(self.times))
        elif self.num < self.entered_num:
            print("Sorry! {} is Big !" .format(self.entered_num))
            if self.count_times >= self.times:
                self.isfinished = True
                print("Sorry! You have used all {} chances." .format(self.times))

    def output_chances(self):
        print("Game continues! You still have {} chances." .format(self.times - self.count_times))

# main program
g = random_game(1,20,10)
while g.isfinished == False:
    # output remaining chances
    g.output_chances()
    # input number
    g.input_num()
    # check if number fits
    g.check()
