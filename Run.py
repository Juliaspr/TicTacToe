from Game1.Game import Game

if __name__ == "__main__":
    try:
        game = Game()
        game.start()
    except KeyboardInterrupt:
        print("Игра окончена!")
