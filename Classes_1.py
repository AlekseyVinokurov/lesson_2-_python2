
# ВАРИАНТ 1 объявления класса с неизвестным количеством аргументов
class example:

    # constructor overloading
    # based on args
    def __init__(self, *args):

        # if args are more than 1
        # sum of args
        if len(args) > 1:
            self.answer = 0
            for i in args:
                self.answer += i

                # if arg is an integer
        # square the arg
        elif isinstance(args[0], int):
            self.answer = args[0] * args[0]

            # if arg is string
        # Print with hello
        elif isinstance(args[0], str):
            self.answer = "Hello! " + args[0] + "."


# Вариант 2: вызов различных инициализаторов в зависимости от числа аргументов
'''
При инициализации объекта определяется количество аргументов
и в зависимости от количества производится вызов метода
'''

class equations_1:

    # single constructor to call other methods
    def __init__(self, *abc):

        # when 2 arguments are passed
        if len(abc) == 2:
            self.ans = self.eq1(abc)

            # when 3 arguments are passed
        elif len(abc) == 3:
            self.ans = self.eq2(abc)

            # when more than 3 arguments are passed
        else:
            self.ans = self.eq3(abc)

    def eq1(self, args):
        x = (args[0] * args[0]) + (args[1] * args[1])
        return x

    def eq2(self, args):
        y = args[0] + args[1] - args[2]
        return y

    def eq3(self, args):
        temp = 0
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / 5.0
        z = temp
        return z


# Вариант 3 создается класс с вызовом методов по обстоятельствам

'''
В данном  примере создаётся класс с множеством методов и
вызов методов определяется в зависимости от решения разраба
на этапе вызова метода для инациализации класса
'''
class equations_2:

    # basic constructor
    def __init__(self, x):
        self.ans = x

    @classmethod
    def eq1(obj, args):
        # create an object for the class to return
        a = obj((args[0] * args[0]) + (args[1] * args[1]))
        return a

    @classmethod
    def eq2(obj, args):
        b = obj(args[0] + args[1] - args[2])
        return b

    @classmethod
    def eq3(obj, args):
        temp = 0

        # square of each element
        for i in range(0, len(args)):
            temp += args[i] * args[i]

        temp = temp / 5.0
        z = obj(temp)
        return z


# Вариант 4

class Myclass_1:
    def __init__(self, x=0):
        self.x = x
class Myclass_2:
    x : int
    def __init__(self):
        pass
    #def __getattribute__(self, attr):
       # return object.__getattribute__(self, attr)  # Только так!!!
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
