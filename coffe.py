class Espresso:
    def grindCoffee(self):
        print("Мелем кафе на фини зърна")

    def makeCoffee(self):
        print("Правим еспресо")

    def pourIntoCup(self):
        print("Сипваме еспресото в чаша")


class Cappuccino:
    def grindCoffee(self):
        print("Мелем кафе на средно груби зърна")

    def makeCoffee(self):
        print("Правим капучино")

    def pourIntoCup(self):
        print("Сипваме капучино в чаша")

class Americano:
    def grindCoffee(self):
        print("Мелем кафе на груби зърна")

    def makeCoffee(self):
        print("Правим американо")

    def pourIntoCup(self):
        print("Сипваме американо в чаша")


class CoffeeFactory:
    def createCoffee(self, coffee_type):
        if coffee_type == "Espresso":
            return Espresso()
        elif coffee_type == "Cappuccino":
            return Cappuccino()
        elif coffee_type == "Americano":
            return Americano()
        else:
            raise ValueError("Неподдържан тип кафе")


if __name__ == "__main__":
    factory = CoffeeFactory()

    espresso = factory.createCoffee("Espresso")
    espresso.grindCoffee()
    espresso.makeCoffee()
    espresso.pourIntoCup()

    cappuccino = factory.createCoffee("Cappuccino")
    cappuccino.grindCoffee()
    cappuccino.makeCoffee()
    cappuccino.pourIntoCup()

    americano = factory.createCoffee("Americano")
    americano.grindCoffee()
    americano.makeCoffee()
    americano.pourIntoCup()
