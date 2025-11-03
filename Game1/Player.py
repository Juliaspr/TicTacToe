class Player:
    
    def __init__(self, name, symbol):
        self.__name = name
        self.__symbol = symbol

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Имя должно быть строкой")

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        if isinstance(value, str) and (value == "x" or value == "o"):
            self.__name = value
        else:
            raise ValueError("Символ должен быть строкой")

    def player_move(self, board):
        while True:
            try:
                row = int(input(f"{self.__name}, введите номер строки: ")) - 1
                col = int(input(f"{self.__name}, введите номер столбца: ")) - 1

                if not (0 <= row < board.n and 0 <= col < board.n):
                    print("Координаты вне диапазона. Попробуйте снова.")
                    continue

                if not board.is_free_cell(row=row, col=col):
                    print("Клетка уже занята. Выберите другую.")
                    continue

                board.update_cell(row=row, col=col, symbol=self.symbol)
                break
            except ValueError:
                print("Строка или столбец должены быть числом!")