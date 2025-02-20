"""
Singleton utilities.
"""


class Singleton(type):
    """
    Implements the Singleton design pattern, allowing only one instance of the object to be created.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the object.
        """
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        Returns the created instance of the object on each class call. If it doesn't exist, creates one.
        """
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance
