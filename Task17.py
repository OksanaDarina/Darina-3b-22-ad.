class Book:
 def __init__(self, title, author, year, genre):
  self.title = title
  self.author = author
  self.year = year
  self.genre = genre

 def info(self):
  print(f"{self.title}, {self.author}({self.year}), {self.genre}")
book = Book("Сияние", "Стивен Кинг", 1977, "готическая литература")
book.info()