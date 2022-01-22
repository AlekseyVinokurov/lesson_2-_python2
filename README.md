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
    x : int = 0
    def __init__(self):
        pass
```
Также можно использовать конструктор с инициализатором:
```python
class Myclass_1:
    def __init__(self, x=0):
        self.x = x
```
