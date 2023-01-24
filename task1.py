import doctest



class Cube:
    def __init__(self, rib: float, material: str):
        """
        Создание и подготовка к работе объекта "Куб"
        :param : Объем стакана
        :param occupied_volume: Объем занимаемой жидкости
        Примеры:
        >>> cube = Cube(500, 'wood')  # инициализация экземпляра класса
        """
        if not isinstance(rib, (int, float)):
            raise TypeError("Ребро должно быть типа int или float")
        if rib <= 0:
            raise ValueError("Ребро стакана должно быть положительным числом")
        self.rib = rib

        if not isinstance(material, str):
            raise TypeError("Материал должен быть str")
        self.material = material

    def get_volume(self) -> int:
        """
        Функция которая вычисляет объем
        :return: объем куба
        Примеры:
        >>> cube = Cube(500, 'wood')
        >>> cube.get_volume()
        """
        ...

    def get_weight(self) -> int:
        """
        Вычисляет вес.
        :return: вес куба
        >>> cube = Cube(500, 'wood')
        >>> cube.get_weight()
        """

        ...

class Bottle:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Бутылка"
        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости
        Примеры:
        >>> glass = Bottle(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def get_weight(self) -> int:
        """
        Функция которая вычисляет вес жидкости в бутылке
        :return: вес жидкости
        Примеры:
        >>> glass = Bottle(500, 0)
        >>> glass.get_weight()
        """
        ...

    def add_water(self, water: float) -> None:
        """
        Добавление воды в стакан.
        :param water: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в стакане, то вызываем ошибку
        Примеры:
        >>> glass = Bottle(500, 0)
        >>> glass.add_water(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...


class Planet:
    def __init__(self,  population: int, animals: list):
        """
        Создание и подготовка к работе объекта "Планета"
        :param size: размер планеты
        :param population: численность населения
        :param animals: список животных, живущих на планете
        Примеры:
        >>> earth = Planet(7000000000, ['dog','cat','lion','tiger'])  # инициализация экземпляра класса
        """
        if not isinstance(population, int):
            raise TypeError("Численность населения должна быть типа int")
        if population <= 0:
            raise ValueError("Численность населения должна  быть положительным числом")
        self.population = population

        if not isinstance(animals, list):
            raise TypeError("Количество жидкости должно быть int или float")
        self.animals = animals

    def add_animal(self, animal: str) -> list:
        """
        Функция которая добавляет новых животных в список
        :param animal: Объем добавляемой жидкости
        :return: список животных
        Примеры:
        >>> earth = Planet(7000000000, ['dog','cat','lion','tiger'])
        >>> earth.add_animal('giraffe')
        """
        if not isinstance(animal, str):
            raise TypeError("Добавляемая переменая должна быть типа str")
        ...

    def add_population(self, people: int) -> int:
        """
        Добавление воды в стакан.
        :param people: Количество добавляемых обитателей
        :raise ValueError: Если количество добавляемых обитателей отрицательное число, то вызываем ошибку
        Примеры:
        >>> earth = Planet(7000000000, ['dog','cat','lion','tiger'])
        >>> earth.add_population(1000000)
        """
        if not isinstance(people, int):
            raise TypeError("Добавляемая переменая должна быть типа int")
        if people < 0:
            raise ValueError("Добавляемая переменая должна быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()
    pass
