BOOKS_DATABASE = [
    {
        "id": 1,  # Идентификатор первой книги
        "name": "test_name_1",  # Название первой книги
        "pages": 200,  # Количество страниц в первой книге
    },
    {
        "id": 2,  # Идентификатор второй книги
        "name": "test_name_2",  # Название второй книги
        "pages": 400,  # Количество страниц во второй книге
    }
]

class Book:
    def __init__(self, id_, name, pages):
        # Конструктор класса Book, принимает параметры:
        # id_ - идентификатор книги
        # name - название книги
        # pages - количество страниц
        self.id = id_  # Присваиваем идентификатор книги атрибуту id
        self.name = name  # Присваиваем название книги атрибуту name
        self.pages = pages  # Присваиваем количество страниц атрибуту pages

    def __str__(self):
        # Метод для строкового представления объекта.
        # Возвращает строку вида: Книга "название книги"
        return f'\u041a\u043d\u0438\u0433\u0430 \"{self.name}\"'

    def __repr__(self):
        # Метод для представления объекта, которое можно использовать для его воссоздания.
        # Возвращает строку вида: Book(id_=id, name='name', pages=pages)
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

if __name__ == '__main__':
    # Главная точка входа в программу

    # Инициализируем список книг из базы данных BOOKS_DATABASE
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проходимся по списку книг и выводим их строковое представление (__str__)
    for book in list_books:
        print(book)  # Вывод: Книга "название книги"

    # Выводим список книг, проверяя метод __repr__ для каждого объекта
    print(list_books)  # Вывод: [Book(id_=1, name='...', pages=...), Book(id_=2, name='...', pages=...)]