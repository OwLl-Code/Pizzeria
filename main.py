"""Код содержит операции по добавлению пицц к заказу, 
удалению пицц из заказа и созданию заказа с определенным количеством сыра. 
Различные исключения, такие как PizzaError и TooMuchCheeseError,
 обрабатываются соответствующим образом с выводом сообщений об ошибках"""

from pizzeria import PizzaError, TooMuchCheeseError, Order


def main():
    pizzeria = Order()

    for pz in ["Margarita", "Capricciosa", "Calzone", "Mafia"]:
        try:
            pizzeria.add_pizza(pz)
        except PizzaError as pe:
            print(pe, ":", pe.pizza)
        except:
            pass

    print()
    print()

    ## Удаление пиццы
    # for pz  in ['Margarita','Capricciosa', 'Calzone', 'Mafia', 'Sdugfskgjf']:
    #    try:
    #         pizzeria.remove_pizza(pz)
    #     except PizzaError as pe:
    #         print(pe, ':', pe.pizza)
    #     except:
    #         pass

    # print()
    # print()

    # Создание заказа
    for pz, ch in [
        ("Margarita", 0),
        ("Capricciosa", 110),
        ("Calzone", 40),
        ("Calzone", 20),
    ]:
        try:
            pizzeria.make_order(pz, ch)
        except TooMuchCheeseError as tmce:
            print(tmce, ":", tmce.cheese)
        except PizzaError as pe:
            print(pe, ":", pe.pizza)
        except:
            pass

    print()
    print()


if __name__ == "__main__":
    print("main.py - Запущено как самостоятельный модуль")
    main()
else:
    print("main.py - Запущено как импортируемый модуль")
