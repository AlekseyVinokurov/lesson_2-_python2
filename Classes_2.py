class Factories:
    def __init__(self, name: str = "Без названия", discription: str = ""):
        self.name = name
        self.description = discription

    def print(self):
        return f'''Фабрика {self.name} Описание {self.description}'''


class Units:
    def __init__(self, name: str = "Без названия", Factoryld: int = 0):
        self.name = name
        self.description = Factoryld

        if isinstance(Factoryld, int) and Factoryld > 0:
            self.Factoryld = Factoryld
        else:
            self.Factoryld = None
    def print(self):
        return f'''Продукт {self.name} Номер фабрики {self.Factoryld}'''

class Tanks:
    def __init__(self,
                 name: str = "Без названия",
                 volume: int = 0,
                 maxVolume: int = 0,
                 unitld: int = 0):
        self.name = name


        if isinstance(volume, int) and volume > 0:
            self.volume = volume
        else:
            self.volume = 0

        if isinstance(maxVolume, int) and maxVolume > 0:
            self.maxVolume = maxVolume
        else:
            self.maxVolume = 0

        if isinstance(unitld, int) and unitld > 0:
            self.unitld = unitld
        else:
            self.unitld = 0

    def print(self):
        s = f'Цистерна: {self.name}; ' \
            f'Емкость: {self.volume}; ' \
            f'Максимальная емкость: {self.maxVolume}; ' \
            f'Номер продукта: {self.unitld}'
        return s