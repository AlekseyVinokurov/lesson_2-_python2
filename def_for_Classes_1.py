from Classes_1 import  Myclass_1
from Classes_1 import  Myclass_2
from Classes_1 import  example
from Classes_1 import  equations_1
from Classes_1 import  equations_2


def def_for_Classes_1 ():
        MyObject_1 = Myclass_1()
        MyObject_1.x = 11.5
        print(MyObject_1.x)
        MyObject_2 = Myclass_2()
        MyObject_2.x = 11.5
        print(MyObject_2.x)


        def printPetNames(owner, **pets):
            print(f"Owner Name: {owner}")
            for a, b in pets.items():
                print(f"{a}: {b}")

        printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")

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

        # Вызов для варианта класса с несколькими конструкторами 3
        li = [[4, 2], [4, 2, 3], [1, 2, 3, 4, 5]]
        i = 0

        while i < 3:

            input = li[i]

            # no.of.arguments = 2
            if len(input) == 2:
                p = equations_2.eq1(input)
                print("equation 1 :", p.ans)

                # no.of.arguments = 3
            elif len(input) == 3:
                p = equations_2.eq1(input)
                print("equation 2 :", p.ans)

                # More than three arguments
            else:
                p = equations_2.eq3(input)
                print("equation 3 :", p.ans)

                # increment loop
            i += 1