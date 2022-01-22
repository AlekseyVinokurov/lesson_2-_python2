# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyObject_1=Myclass_1()
    MyObject_1.x = 11.5
    print(MyObject_1.x)
    MyObject_2=Myclass_1()
    MyObject_2.x = 11.5
    print(MyObject_2.x)
    print_hi('Aleksey')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
