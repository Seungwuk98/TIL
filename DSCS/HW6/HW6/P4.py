class Calculator:
    def __init__(self):
        # write your code below
        self.result = 0
        self.num = 0
        self.operator = '+'

    def digit(self, num):
        # write your code below
        self.num = self.num*10 + num

    def plus(self):
        # write your code below
        self.calculate()
        self.operator = '+'

    def minus(self):
        # write your code below
        self.calculate()
        self.operator = '-'

    def clear(self):
        # write your code below
        self.result = 0
        self.num = 0
        self.operator = '+'

    def equal(self):
        # write your code below
        self.calculate()
        ret = self.result
        self.clear()
        return ret

    def calculate(self):
        self.result += self.num if self.operator == '+' else -self.num
        self.num = 0
        self.operator = '+'
