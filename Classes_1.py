
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


# Вариант kwargs Класс с таблицей и словарем

class example_3:

    def __init__(self, **kwargs):
        self.ans = kwargs

    def __str__(self):
        s: str = ""

        for kwarg, name in self.ans.items():
            s += f"{kwarg}: {name} \n"
        return (s)



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


### Примеры работы с классами (перезагрузка, собственные классы)
class MyClass_3:
    x = int
    def __init__(self, x = int): # Конструктор
        self.x = 10 # Атрибут экземпляра класса
    def print_x(self): # self — это ссылка на экземпляр класса
        print(self.x) # Выводим значение атрибута
    def __getattr__(self, item):
        print("не получается")
        return 0
    def __len__(self):
        i = 0
        n=self.x
        while n > 0:
            n = n // 10
            i += 1
        return i

class MyNomber:
    def __init__(self, nunber = 0): # Конструктор
        self.x = nunber # Атрибут экземпляра класса
    def __add__(self, other):
        return self.x + other

    def __add__(self, other):
        if isinstance(other, MyNomber):
            return self.x + other.x
        else:
            return self.x + other

    def __len__(self):
        i = 0
        n = self.x
        while n > 0:
            n = n // 10
            i+=1
        return i
    def __str__(self):
        print(self.x)

class MyPercentClass:
    x=0;
    def __init__(self, number=0): # Конструктор
        self.x = number/100

    def get_value(self, number):
        self.x = number/100
        return self.x


    def __add__(self, other):
        if isinstance(other, MyPercentClass):
            return self.x + other.x
        else:
            return self.x*other + other

    def __radd__(self, other):
        if isinstance(other, MyPercentClass):
            return self.x + other.x
        else:
            return self.x*other + other

    def __mul__(self, other):
        if isinstance(other, MyPercentClass):
            return self.x + other.x
        else:
            return self.x*other

    def __rmul__(self, other):
        if isinstance(other, MyPercentClass):
            return self.x + other.x
        else:
            return self.x*other

    def __str__(self):
        #print(f"{self.x*100}")
        return str(self.x*100)+"%"


class GetSetDemonstration_1:
    def __init__(self, name = "Без имени", age = 0):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age
    def set_age (self, age):
        if 1< age < 100:
            self.__age = age
        else:
            print(" Недопустимый возраст")

    def get_name(self):
        return self.__name
    def set_name (self, name):
        self.__name = str(name)


class GetSetDemonstration_2:
    def __init__(self, name = "Без имени", age = 0):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age (self, age):
        if 1< age < 100:
            self.__age = age
        else:
            print(" Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name (self, name):
        self.__name = str(name)