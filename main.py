if __name__ == "__main__":
    from sys import exit
    from importlib import reload
    from codigos.menu import menu
    while True:
        op = menu()
        if op:
            import game
            reload(game)
            game.run()
        else:
            exit(0)
