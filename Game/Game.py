from random import choice as get_random_symbol

class Game:

    def __init__(self):
        symbols = ["X", "O"]

        change_n = input("Вы хотите задать пользовательские размеры поля? (Да/Нет): ").strip().lower()

        if change_n == "да":
            while True:
                n_board = input("Введите размерность поля: ").strip()

                try:
                    if not n_board.isdigit() or int(n_board) < 3 or int(n_board) > 10:
                        raise ValueError("Размерность поля должна быть целым числом и не меньше 3 и не больше 10!")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                    continue

                self.board = Board(n = int(n_board))
                break
        else:
            self.board = Board()


        symbol_player1 = get_random_symbol(symbols)
        # name_player1 = input("Игрок №1, введите имя: ")
        name_player1 = "Николай"
        self.player1 = Player(name=name_player1, symbol=symbol_player1)

        symbol_player2 = "X" if symbol_player1 == "O" else "O"
        # name_player2 = input("Игрок №2, введите имя: ")
        name_player2 = "Андрей"
        self.player2 = Player(name=name_player2, symbol=symbol_player2)

        self.current_player = self.player1 if self.player1.symbol == "X" else self.player2

        print(f"\n{self.player1.name} играет за {self.player1.symbol}\n{self.player2.name} играет за {self.player2.symbol}\nПервыми ходят крестики:\n")


    def start(self):
        print(self.board)

        while True:
            self.current_player.player_move(self.board)
            self.board.display()
            result = self.board.check_win(current_player=self.current_player)

            if result == 1:
                print(f"Победил игрок: {self.current_player.name}!")
                break
            elif result == 0:
                print(f"Ничья!")
                break
            else:
                self.current_player = self.player1 if self.current_player == self.player2 else self.player2