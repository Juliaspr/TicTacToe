class Board:

    def __init__(self, n: int = 3):
        self.__n = n
        self.__board = [["*" for _ in range(self.__n)] for _ in range(self.__n)]


    def __str__(self):
        board_txt = ""
        board_txt += " ".join([" "] + [str(i) for i in range(1, self.__n + 1)]) + "\n"

        for row_index, row in enumerate(self.__board, 1):
            board_txt += f"{row_index} {' '.join(row)}\n"

        return board_txt

    @property
    def n(self):
        return self.__n

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, new_board):
        self.__board = new_board

    def is_free_cells(self):
        return any(cell == "*" for row in self.__board for cell in row)

    def is_free_cell(self, row, col):
        return self.__board[row][col] == "*"

    def display(self):
        column = [" "] + [i for i in range(1, self.__n + 1)]
        print(*column)

        for row in range(self.__n):
            print(f"{row + 1} {' '.join(self.__board[row])}")

    def update_cell(self, row, col, symbol):
        self.__board[row][col] = symbol


    def check_win(self, current_player):

        for i in range(self.n):

            if all(self.board[i][j] == current_player.symbol for j in range(self.n)):
                return 1

            if all(self.board[j][i] == current_player.symbol for j in range(self.n)):
                return 1

        if all(self.board[i][i] == current_player.symbol for i in range(self.n)):
            return 1

        if all(self.board[i][self.n - 1 - i] == current_player.symbol for i in range(self.n)):
            return 1

        if not self.is_free_cells():
            return 0

        return -1