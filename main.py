# -*- coding: utf-8 -*-
from ZabavyCloud.context import Context


def main():
    print("Running main.")
    with Context() as app:
        app.loop(context=app)
    print("Main finished.")


if __name__ == '__main__':
    main()
