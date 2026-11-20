from enum import Enum


class CandyType(Enum):
    BAR = "bar"
    BUTTON = "button"
    POPCORN = "popcorn"
    GUM = "gum"


class Candy:
    def __init__(self, name, mass, amount, price, candy_type):
        self._name = ""
        self._mass = 0
        self._amount = 0
        self._price = 0
        self._candy_type = None

        self.name = name
        self.mass = mass
        self.amount = amount
        self.price = price
        self.candy_type = candy_type

    def __del__(self):
        print(f"Candy '{self._name}' was deleted")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        if value > 0:
            self._mass = value
        else:
            print("Error: mass must be greater than 0")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value >= 0:
            self._amount = value
        else:
            print("Error: amount cannot be negative")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Error: price cannot be negative")

    @property
    def candy_type(self):
        return self._candy_type

    @candy_type.setter
    def candy_type(self, value):
        self._candy_type = value

    def ate(self):
        if self.mass * self.amount > 2000:
            return f"{self.name}: You’re on a diet!"
        return f"{self.name}: What delicious candies!"

    def show_info(self):
        print(f"{self.name} ({self.candy_type.value}): "
              f"{self.mass}g, {self.amount}pcs, "
              f"price: {self.price}₴")


def find_the_most_expensive_candies(candies, name=None):
    matching = (item for item in candies if name is None or item.name == name)
    return sorted(matching, key=lambda item: item.price, reverse=True)[:3]
    filtered = []
    for candy in candies:
        if name is None or candy.name == name:
            filtered.append(candy)

    filtered.sort(key=lambda candy: candy.price, reverse=True)
    return filtered[:3]


class Dinner:
    def __init__(self, day, time):
        self._day = ""
        self._time = ""
        self.day = day
        self.time = time
        self._candies = []

    def __del__(self):
        print(f"Dinner ({self._day}, {self._time}) was deleted")

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def candies(self):
        return self._candies

    def add_candy(self, candy):
        self._candies.append(candy)

    def sort_candies(self, parameter, reverse=False):
        if parameter == "name":
            self._candies.sort(
                key=lambda candy: candy.name, reverse=reverse)
        elif parameter == "mass":
            self._candies.sort(
                key=lambda candy: candy.mass, reverse=reverse)
        elif parameter == "amount":
            self._candies.sort(
                key=lambda candy: candy.amount, reverse=reverse)
        elif parameter == "price":
            self._candies.sort(
                key=lambda candy: candy.price, reverse=reverse)
        else:
            print("Error: unknown sorting parameter")

    def show_info(self):
        print(f"Dinner: {self._day} {self._time}")
        for candy in self._candies:
            candy.show_info()


def main():
    dinner = Dinner("Monday", "13:00")
    orbit = Candy("Orbit", 14, 2, 25, CandyType.GUM)
    milka = Candy("Milka", 250, 2, 115, CandyType.BAR)
    popcorn = Candy("Popcorn", 500, 5, 60, CandyType.POPCORN)
    dinner.add_candy(orbit)
    dinner.add_candy(milka)
    dinner.add_candy(popcorn)

    dinner.show_info()

    print("Method ate:")
    for candy in dinner.candies:
        print(candy.ate())

    print("Sorting by name:")
    dinner.sort_candies("name")
    dinner.show_info()

    print("Sorting by mass:")
    dinner.sort_candies("mass", reverse=True)
    dinner.show_info()

    print("Top 3 most expensive candies:")
    for candy in find_the_most_expensive_candies(dinner.candies):
        candy.show_info()

    print("Changing price through setter:")
    milka.price = 99
    milka.show_info()


if __name__ == "__main__":
    main()