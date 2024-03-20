from os import strerror


class PizzaError(Exception):
    """Класс определяющий ошибку в названии пиццы"""

    def __init__(self, pizza, message):
        self.pizza = pizza
        self.message = message


class TooMuchCheeseError(Exception):
    """Класс определяющий ошибку в количестве сыра"""

    def __init__(self, pizza, cheese, message):
        self.cheese = cheese
        self.pizza = pizza
        self.message = message


class Pizza:
    list = ["Margarita", "Capricciosa", "Calzone"]

    def __init__(self):
        self.pizza = ""
        self.pizza_to_remove = ""

    def add_pizza(self, pizza):
        self.pizza = pizza
        if self.pizza in Pizza.list:
            raise PizzaError(self.pizza, "Пицца уже существует!")

        Pizza.list.append(self.pizza)
        print(f"{self.pizza} : Успешно добавлена в список пицц!\nlist: {Pizza.list}")

    def remove_pizza(self, pizza):
        self.pizza_to_remove = pizza
        if self.pizza_to_remove not in Pizza.list:
            raise PizzaError(self.pizza, "Пиццы не существует!")

        Pizza.list.remove(self.pizza_to_remove)
        print(f"{self.pizza} : Успешно удалена из списка пицц!\nlist: {Pizza.list}")


class Order(Pizza):
    def __init__(self):
        super().__init__()
        self.order = {}
        self.counter = 1
        self.fo = open("pizzas_order.txt", "wt")
        self.fo.close()

    def make_order(self, pizza, cheese):
        self.mpizza = pizza
        self.cheese = cheese

        if self.mpizza not in Pizza.list:
            raise PizzaError(self.mpizza, "Такой пиццы нет!")

        if self.cheese > 100:
            raise TooMuchCheeseError(self.mpizza, self.cheese, "Слишком много сыра")

        self.order.update({self.counter: f"{self.mpizza} с {self.cheese} сыром"})
        print(f"Заказ {self.counter}: {self.order[self.counter]} успешно создан")

        try:
            self.fo = open("pizzas_order.txt", "at")
            result_order = f"{self.counter} {self.mpizza} с {self.cheese} сыром. \n\n"
            self.fo.write(result_order)
            print("Успешно записано в файл")
        except IOError as e:
            print("Ошибка - ", strerror(e.errno))
        finally:
            self.fo.close()
            self.counter += 1


if __name__ == "__main__":
    print("Запущено как самостоятельный модуль")
else:
    print("Запущено как импортируемый модуль")
