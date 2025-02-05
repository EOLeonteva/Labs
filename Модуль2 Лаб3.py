class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        # Конструктор класса, инициализирует объект книги с названием и автором
        # name (str): название книги
        # author (str): автор книги
        # Используем защищенные атрибуты, чтобы предотвратить их изменение извне
        self._name = name  # Название книги
        self._author = author  # Автор книги

    @property
    def name(self):
        # Геттер для получения названия книги, нельзя изменить после создания
        return self._name

    @property
    def author(self):
        # Геттер для получения автора книги, нельзя изменить после создания
        return self._author

    def __str__(self):
        # Метод для возврата строкового представления объекта для пользователей
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        # Метод для возврата строкового представления объекта для отладки
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс бумажной книги, наследуется от Book. """
    def __init__(self, name: str, author: str, pages: int):
        # Конструктор класса, вызывает конструктор родителя и устанавливает количество страниц
        super().__init__(name, author)
        self.pages = pages  # Устанавливаем количество страниц через сеттер

    @property
    def pages(self):
        # Геттер для получения количества страниц книги
        return self._pages

    @pages.setter
    def pages(self, value):
        # Сеттер для установки количества страниц с проверкой корректности
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = value  # Присваивание корректного значения

    def __str__(self):
        # Метод для возврата строкового представления объекта с дополнительной информацией
        return f"{super().__str__()}. Страниц: {self.pages}"


class AudioBook(Book):
    """ Класс аудиокниги, наследуется от Book. """
    def __init__(self, name: str, author: str, duration: float):
        # Конструктор класса, вызывает конструктор родителя и устанавливает длительность
        super().__init__(name, author)
        self.duration = duration  # Устанавливаем продолжительность книги через сеттер

    @property
    def duration(self):
        # Геттер для получения продолжительности аудиокниги
        return self._duration

    @duration.setter
    def duration(self, value):
        # Сеттер для установки продолжительности с проверкой корректности
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = float(value)  # Присваивание корректного значения

    def __str__(self):
        # Метод для возврата строкового представления объекта с дополнительной информацией
        return f"{super().__str__()}. Длительность: {self.duration} часов"