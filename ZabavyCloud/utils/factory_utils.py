"""
Factory Utilities.
"""


class Factory:
    """
    The Factory class represents a factory. It has one method, create, which
    takes one required parameter, factory_type, which is a string representing the type
    of factory to create.
    """

    def __repr__(self):
        return f'Factory class.'

    def __str__(self):
        return f'Factory class. {self.factories}'

    def create(self, factory_type: str, *args, **kwargs):
        """
        The create method takes one required parameter, factory_type,
        which is a string representing the type of factory to create.
        """
        if factory_type in self.factories:
            return self.factories[factory_type](*args, **kwargs)
        else:
            raise ValueError(f'Unknown factory type: {factory_type}.')
