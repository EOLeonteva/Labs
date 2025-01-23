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
        # Конструктор класса Book
        self.id = id_  # Устанавливаем идентификатор книги
        self.name = name  # Устанавливаем название книги
        self.pages = pages  # Устанавливаем количество страниц

    def __str__(self):
        # Метод для строкового представления книги
        return f'Книга "{self.name}"'  # Возвращает строку вида "Книга "название""

    def __repr__(self):
        # Метод для представления объекта, которое можно использовать для его воссоздания
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"  # Возвращает строку-конструктор объекта

class Library:
    def __init__(self, books=None):
        # Конструктор класса Library, принимает список книг или инициализирует пустой список
        self.books = books if books is not None else []  # Если список книг не передан, создаем пустую библиотеку

    def get_next_book_id(self):
        # Метод для получения следующего идентификатора книги
        if not self.books:  # Если список книг пуст
            return 1  # Возвращаем идентификатор 1 для первой книги
        return self.books[-1].id + 1  # Возвращаем идентификатор последней книги + 1

    def get_index_by_book_id(self, book_id):
        # Метод для получения индекса книги по её идентификатору
        for index, book in enumerate(self.books):  # Перебираем книги с их индексами
            if book.id == book_id:  # Если идентификатор книги совпадает с запрашиваемым
                return index  # Возвращаем индекс
        raise ValueError("Книги с запрашиваемым id не существует")  # Если книга не найдена, выбрасываем ошибку

if __name__ == '__main__':
    # Точка входа в программу

    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]  # Создаем список книг из базы данных

    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1
