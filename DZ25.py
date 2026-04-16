class Book:

    def input_info(self, name, year, public, genre, author, price):
        self.name = name
        self.year = year
        self.public = public
        self.genre = genre
        self.author = author
        self.price = price

    def print_info(self):
        print("Информация о книге".center(20,"*"))
        print("Название: ", self.name)
        print("Год: ", self.year)
        print("Издатель: ", self.public)
        print("Жанр: ", self.genre)
        print("Автор: ", self.author)
        print("Цена: ", self.price)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_public(self, public):
        self.public = public

    def get_public(self):
        return self.public



b1 = Book()
b1.input_info("Тайна третьей планеты", "1999", "Эксмо", "Фантастика", "Братья Гримм", "230")
b1.print_info()

