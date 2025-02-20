from abc import ABC, abstractmethod

from ..constants.collection import Collection


class Repository(ABC):
    """
    Base for a data repository.
    """

    @abstractmethod
    def read(self, collection: Collection, record: str, skip: int = 0, limit: int = 100) -> list:
        """
        ? Gets a record from the repository.
        """
        pass

    @abstractmethod
    def create(self, collection: Collection, data: dict) -> dict:
        """
        ? Creates a new record in the repository.
        """
        pass

    @abstractmethod
    def update(self, collection: Collection, record: str, data: dict) -> dict:
        """
        ? Updates an element from the repository.
        """
        pass

    @abstractmethod
    def delete(self, collection: Collection, record: str, reason: str) -> dict:
        """
        ? Deletes an element from the repository.
        """
        pass
