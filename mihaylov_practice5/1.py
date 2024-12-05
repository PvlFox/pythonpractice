import pickle

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - {self.genre}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        try:
            self.borrowed_books.remove(book)
        except ValueError:
            raise ValueError(f"{book} was not borrowed by {self.name}")

    def __str__(self):
        borrowed_books_str = ', '.join(str(book) for book in self.borrowed_books)
        return f"Reader: {self.name} (ID: {self.reader_id})\nBorrowed books: {borrowed_books_str if borrowed_books_str else 'No books borrowed'}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        try:
            self.books.remove(book)
        except ValueError:
            raise ValueError(f"The book '{book}' is not in the library.")

    def register_reader(self, reader):
        self.readers.append(reader)

    def lend_book(self, reader, book):
        if book not in self.books:
            raise ValueError(f"The book '{book}' is not available in the library.")
        reader.borrow_book(book)
        self.books.remove(book)

    def return_book(self, reader, book):
        if book not in reader.borrowed_books:
            raise ValueError(f"Reader {reader.name} did not borrow '{book}'.")
        reader.return_book(book)
        self.books.append(book)

    def find_book(self, title=None, author=None):
        results = []
        for book in self.books:
            if title and title.lower() in book.title.lower():
                results.append(book)
            elif author and author.lower() in book.author.lower():
                results.append(book)
        return results

    def get_reader_books(self, reader):
        return reader.borrowed_books

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None

# Пример использования:
# Создаем библиотеку и добавляем книги
library = Library("City Library")
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
book3 = Book("1984", "George Orwell", 1949, "Dystopian")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Регистрируем читателя
reader = Reader("John Doe", 1)
library.register_reader(reader)

# Выдаем книгу
library.lend_book(reader, book1)
print(reader)

# Поиск книг
search_results = library.find_book(title="1984")
print("Search Results:", search_results)

# Возвращаем книгу
library.return_book(reader, book1)
print(reader)

# Сохраняем состояние библиотеки в файл
library.save_to_file("library_state.pkl")

# Загружаем состояние библиотеки из файла
loaded_library = Library.load_from_file("library_state.pkl")
if loaded_library:
    print("Library loaded successfully.")
else:
    print("Failed to load library.")