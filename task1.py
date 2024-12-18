import doctest

class Tree:
    def __init__(self, height: float, age: int, species: str):
        """
        Базовый класс для описания дерева.

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах
        :param species: Вид дерева

        Примеры:
        >>> tree = Tree(10.5, 15, "Oak")
        """
        # Проверяем, что высота задана положительным числом типа int или float
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")
        # Проверяем, что возраст задан целым числом и не является отрицательным
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным числом.")
        # Проверяем, что вид дерева указан строкой и не пустой
        if not isinstance(species, str) or not species:
            raise ValueError("Вид дерева должен быть непустой строкой.")
        # Устанавливаем атрибуты объекта
        self.height = height
        self.age = age
        self.species = species

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева и его высоту.

        :param years: Количество лет роста
        :raise ValueError: Если количество лет отрицательное

        Примеры:
        >>> tree = Tree(10, 10, "Pine")
        >>> tree.grow(5)
        """
        # Метод увеличивает возраст дерева и его высоту (заглушка)
        ...

    def photosynthesize(self) -> None:
        """
        Симулирует процесс фотосинтеза.

        Примеры:
        >>> tree = Tree(15, 20, "Maple")
        >>> tree.photosynthesize()
        """
        # Метод симулирует процесс фотосинтеза (заглушка)
        ...

    def shed_leaves(self) -> None:
        """
        Симулирует сброс листвы деревом.

        Примеры:
        >>> tree = Tree(8, 5, "Birch")
        >>> tree.shed_leaves()
        """
        # Метод симулирует сброс листвы деревом (заглушка)
        ...


class FruitTree(Tree):
    def __init__(self, height: float, age: int, species: str, fruit_type: str, annual_yield: float):
        """
        Класс для описания фруктового дерева.

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах
        :param species: Вид дерева
        :param fruit_type: Тип фрукта, который выращивает дерево
        :param annual_yield: Средний годовой урожай в килограммах

        Примеры:
        >>> fruit_tree = FruitTree(5, 3, "Apple", "Apple", 50.0)
        """
        # Вызываем конструктор базового класса для установки общих параметров дерева
        super().__init__(height, age, species)
        # Проверяем, что тип фрукта задан строкой и не пустой
        if not isinstance(fruit_type, str) or not fruit_type:
            raise ValueError("Тип фрукта должен быть непустой строкой.")
        # Проверяем, что годовой урожай задан неотрицательным числом типа int или float
        if not isinstance(annual_yield, (int, float)) or annual_yield < 0:
            raise ValueError("Годовой урожай должен быть неотрицательным числом.")
        # Устанавливаем атрибуты объекта
        self.fruit_type = fruit_type
        self.annual_yield = annual_yield

    def harvest(self) -> float:
        """
        Симулирует сбор урожая с дерева.

        :return: Количество собранного урожая в килограммах

        Примеры:
        >>> fruit_tree = FruitTree(6, 4, "Peach", "Peach", 30.0)
        >>> fruit_tree.harvest()
        30.0
        """
        # Метод симулирует сбор урожая с дерева (заглушка)
        ...

    def bloom(self) -> None:
        """
        Симулирует процесс цветения дерева.

        Примеры:
        >>> fruit_tree = FruitTree(7, 5, "Cherry", "Cherry", 20.0)
        >>> fruit_tree.bloom()
        """
        # Метод симулирует процесс цветения дерева (заглушка)
        ...

    def produce_fruit(self) -> None:
        """
        Симулирует процесс образования плодов на дереве.

        Примеры:
        >>> fruit_tree = FruitTree(4, 2, "Plum", "Plum", 25.0)
        >>> fruit_tree.produce_fruit()
        """
        # Метод симулирует процесс образования плодов на дереве (заглушка)
        ...


class ConiferousTree(Tree):
    def __init__(self, height: float, age: int, species: str, needle_length: float):
        """
        Класс для описания хвойного дерева.

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах
        :param species: Вид дерева
        :param needle_length: Средняя длина иголок в сантиметрах

        Примеры:
        >>> conifer_tree = ConiferousTree(15, 50, "Pine", 5.0)
        """
        # Вызываем конструктор базового класса для установки общих параметров дерева
        super().__init__(height, age, species)
        # Проверяем, что длина иголок задана положительным числом типа int или float
        if not isinstance(needle_length, (int, float)) or needle_length <= 0:
            raise ValueError("Длина иголок должна быть положительным числом.")
        # Устанавливаем атрибуты объекта
        self.needle_length = needle_length

    def produce_resin(self) -> None:
        """
        Симулирует процесс выделения смолы деревом.

        Примеры:
        >>> conifer_tree = ConiferousTree(20, 80, "Spruce", 4.0)
        >>> conifer_tree.produce_resin()
        """
        # Метод симулирует процесс выделения смолы деревом (заглушка)
        ...

    def grow_cones(self) -> None:
        """
        Симулирует процесс роста шишек на дереве.

        Примеры:
        >>> conifer_tree = ConiferousTree(10, 30, "Fir", 3.5)
        >>> conifer_tree.grow_cones()
        """
        # Метод симулирует процесс роста шишек на дереве (заглушка)
        ...

    def shed_needles(self) -> None:
        """
        Симулирует сброс иголок деревом.

        Примеры:
        >>> conifer_tree = ConiferousTree(12, 40, "Cedar", 6.0)
        >>> conifer_tree.shed_needles()
        """
        # Метод симулирует сброс иголок деревом (заглушка)
        ...

if __name__ == "__main__":
    doctest.testmod()
