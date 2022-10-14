class Plus:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self):
         return f'\nпервое число: {self.num1}\nвторое число: {self.num2} ' \
                f'\nдействие: сложение \nответ:{self.num1 + self.num2}'

class Minus:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


    def __sub__(self):
         return f'\nпервое число: {self.num1}\nвторое число: {self.num2} ' \
                f'\nдействие: вычитание \nответ:{self.num1 - self.num2}'

class Umnozh:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __mul__(self):
         return f'\nпервое число: {self.num1}\nвторое число: {self.num2} ' \
                f'\nдействие: умножение \nответ:{self.num1 * self.num2}'

class Delen:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def __truediv__(self):
         return f'\nпервое число: {self.num1}\nвторое число: {self.num2} ' \
                f'\nдействие: деление \nответ:{self.num1 / self.num2}'

class Calculator(Plus,Minus,Umnozh,Delen):
    def __init__(self,num1,num2):
        Plus.__init__(self, num1, num2)
        Minus.__init__(self, num1, num2)
        Umnozh.__init__(self, num1, num2)
        Delen.__init__(self, num1, num2)


a =Calculator(6,3)
print(a.__add__())

b =Calculator(6,3)
print(b.__sub__())

c =Calculator(6,3)
print(c.__mul__())

d =Calculator(6,3)
print(d.__truediv__())