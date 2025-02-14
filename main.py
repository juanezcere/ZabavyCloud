# -*- coding: utf-8 -*-
from app import Zabavy


def main():
    print("Running main.")
    with Zabavy() as zabavy:
        # zabavy.start(layout=0) # ? <== To start the game directly
        zabavy.run()
    print("Main finished.")


if __name__ == '__main__':
    main()
