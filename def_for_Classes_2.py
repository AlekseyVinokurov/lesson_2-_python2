from Classes_2 import Factories
from Classes_2 import Units
from Classes_2 import Tanks

def def_for_Classes_2 ():
    arr_Factories = []
    arr_Factories.append(Factories("НПЗ#1", "Первый нефтеперерабатывающий завод"))
    arr_Factories.append(Factories("НПЗ#2", "Второй нефтеперерабатывающий завод"))

    # print(len(arr_Factories))
    # print(arr_Factories[1].name)

    arr_Units = []
    arr_Units.append(Units("ГФУ-2", 1))
    arr_Units.append(Units("АВТ-6", 1))
    arr_Units.append(Units("АВТ-10", 2))
    arr_Units.append(Units("АВТ-10", '2'))

    # print(len(arr_Units))
    # print(arr_Units[3].Factoryld)

    arr_Tanks = []
    arr_Tanks.append(Tanks("Резервуар 1", 1500, 2000, 1))
    arr_Tanks.append(Tanks("Резервуар 2", 2500, 3000, 1))
    arr_Tanks.append(Tanks("Дополнительный резервуар 24", 3000, 3000, 2))
    arr_Tanks.append(Tanks("Резервуар 35", 3000, 3000, 2))
    arr_Tanks.append(Tanks("Резервуар 5", 4000, 5000, 2))
    arr_Tanks.append(Tanks("Резервуар 6", 500, 500, 3))

    # print(arr_Tanks[3].maxVolume)

    print("")
    for i in arr_Factories:
        print(i.print())
    print("")
    for i in arr_Units:
        print(i.print())
    print("")
    for i in arr_Tanks:
        print(i.print())
    print("")