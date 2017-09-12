import random

class random_game:
    def __init__(self, from_num, to_num, digits, times):
        self.from_num = from_num
        self.to_num = to_num
        self.digits = digits
        self.times = times
        self.num = []
        self.enter_num = []
        self.count_times = 0
        self.isfinished = False

    # get a random number not beggining with 0
    def random_num(self):
        digit_range = range(self.from_num, self.to_num)
        self.num = random.sample(digit_range, self.digits)
        while self.num[0] == 0:
            self.num = random.sample(digit_range, self.digits)
        #print(self.num) #for debug

    # get the input number and check whether it is complied with the criteria - 4 differnt digits
    def input_num(self):
        self.enter_num = []
        input_str = input("Pls enter a 4-differnt-digit number between 1000 to 9999: ")
        while input_str.isdigit() == False or len(input_str) != self.digits or len(input_str) != len(set(input_str)) :
            print("{} is not correct" .format(input_str))
            input_str = input("Please enter a 4-differnt-digit number between 1000 and 9999：")

        for i in input_str:
            self.enter_num.append(int(i))
            #print(self.enter_num)

        self.count_times = self.count_times + 1

    # check whether the number and position are correct or not
    def check(self):
        a = b = 0 # a means correct number and position; b means correct number but with wrong positon
        for x in range(0,self.digits):
            if self.num[x] == self.enter_num[x]:
                a += 1
            if self.enter_num[x] in self.num and self.enter_num[x] != self.num[x]:
                b += 1
        if a == self.digits:
            self.isfinished = True
            print("Congratulations! You are correct!")
        else:
            print (f"{a}A{b}B. Pls continue")

    # check the chances used and left
    def time_count(self):
        if self.count_times == self.times:
            self.isfinished = True
            print("Sorry, no chance left. The correct answer should be {}".format(self.num[0]*1000 + self.num[1]*100 + self.num[2]*10 + self.num[3]))
        else:
            print("You still have {} chances left.".format(self.times - self.count_times))

play = random_game(0,10,4,10)
play.random_num()
while play.isfinished == False:
    play.input_num()
    play.check()
    if play.isfinished == True:
        break
    play.time_count()
