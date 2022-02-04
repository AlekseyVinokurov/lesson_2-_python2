# Урок работы с переменными классами и типами (python_lesson_2)
Варианты создания классов и объектов
Простой класс можно создавать конструкцией:
```python
class Myclass_2:
    x : int
    def __init__(self):
        pass
```
В этом случае если создать объект класса `MyObject_2=Myclass_2()` , то при попытке вызова свойства возникнет ошибка
> **AttributeError: 'Myclass_2' object has no attribute 'x'**

Требуется выполнять последовательость: инициализация объукта, указание свойства, вызов свойства:
```python
MyObject_2=Myclass_2()
    MyObject_2.x = 11.5
    print(MyObject_2.x)
```
или создавать класс со значением поля по умолчанию:
```python
class Myclass_2:
    x : int = 0 # Атрибут объекта класса
    def __init__(self):
        pass
```
Также можно использовать конструктор с инициализатором:
```python
class Myclass_1:
    def __init__(self, x=0):
        self.x = x # Атрибут экземпляра класса
```
### Пример отличия **Атрибут объекта класса** от **Атрибут экземпляра класса**
> Создаем класс:
```python
class MyClass:
    x = 10 # Атрибут объекта класса
    def __init__(self):
        self.y = 20 # Атрибут экземпляра класса
```
> Создаем экземпляры классов
```python
c1 = MyClass() # Создаем экземпляр класса
c2 = MyClass() # Создаем экземпляр класса
print(c1.x, c2.x) # 10 10
```
> Изменяем атрибут объекта класса, посмотрим результат
*Ожидается изменение во всех объектах*
```python
MyClass.x = 88 # Изменяем атрибут объекта класса
print(c1.x, c2.x) # 88 88
```
> Изменяем атрибут экземпляра класса
*Ожидается изменение *
```python
print(c1.x, c2.x) # 10 10
MyClass.x = 88 # Изменяем атрибут объекта класса
print(c1.x, c2.x) # 88 88
```
### Пример работы с классами с неопределённым количеством аргументов
Класс может содержать определенное и неопределенные заранее количество аргуменнтов
> В данном примере показана ситуации когда при объявлении класса может быть получено неограниченное количество аргументов. При этом в зависимости от количества и Типа аргументов применяются различные операции. Если один целочисленный аргумент- вычисляется квадрат числа, если один строковый аргумент то выводится строка .....
```python
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
```
В данном примере показано применение различных методов классов к аргументам в зависимоти от их количества. Результат зависит от числа аргументов.
```python
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
```
В данном примере класс реализует несколько примеров и на этапе объявления инстанса класса в зависимости от числа аргументов вызывается метод ......
```python
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
```
Вызов для класса с несколькими аргументами
```python
e1 = example(1, 2, 3, 6, 8)
        print("Sum of list :", e1.answer)

        e2 = example(6)
        print("Square of integer :", e2.answer)

        e3 = example("Programmers")
        print("String :", e3.answer)

        abc1 = equations_1(4, 2)
        abc2 = equations_1(4, 2, 3)
        abc3 = equations_1(1, 2, 3, 4, 5)

        print("equation 1 :", abc1.ans)
        print("equation 2 :", abc2.ans)
        print("equation 3 :", abc3.ans)

```
### Работа с классами перезагрузка методолв и операторов

> Данный класс отражает реализацию собственного метода **print_x** ......
```python
class MyClass:
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
        return  i

```
> Вызовы MyClass


```python
c = MyClass() # Создание экземпляра класса
    # Вызываем метод print_x()
    c.print_x () # self не указывается при вызове метода
    print(c.x) # К атрибуту можно обратиться непосредственно
    res_1 = c.__getattribute__("x")
    try:
        setattr(c, "x", 205789)
    except:
        res_1 = False
    else:
        res_1 = True

    print(res_1)

    # Пример попытки вызова несуществующих аргументов
    # с возвратом  0 и выводом текста "не получается"

    a = c.z
    print("Вывожу:", a)



    a = len(c)
    print("Вывожу len(c):", a)


```
> Вданном примере представлен собственный тип листа с операциями над ним

```python
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

```
Вызов
```python
number_1 = MyNomber(17)
    number_2 = MyNomber(10)
    x = number_1+80
    x = number_1 + number_2
    print(x)


```



> Проценты

```python
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

```
Вызов
```python
perc = MyPercentClass()
    perc.get_value(10)
    print(perc)
    per=300+perc
    print(per)
    per=250*perc.get_value(20)
    print(per)

    perc=perc



```


## TODO
- [ ] Написать собственный класс процентов
- [ ] Чётко выделить разницу поле / свойство
- [ ] Привести пример работы с множеством аргументов с применением KEYWarks
- [ ] Привести примеры наследования.
- [ ] Продолжить работы с примером.
