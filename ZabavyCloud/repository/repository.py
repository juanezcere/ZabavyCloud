from abc import ABC, abstractmethod

from ..constants.collection import Collection


class Repository(ABC):
    """
    Base for a data repository.
    """

    @abstractmethod
    def get(self, collection: Collection, filters: str, skip: int = 0, limit: int = 100) -> list:
        """
        ? Gets a register from the repository.
        """
        pass

    @abstractmethod
    def post(self, collection: Collection, data: dict) -> dict:
        """
        ? Creates a new register in the repository.
        """
        pass

    @abstractmethod
    def put(self, collection: Collection, register: str, data: dict) -> dict:
        """
        ? Updates an element from the repository.
        """
        pass

    @abstractmethod
    def delete(self, collection: Collection, register: str, reason: str) -> dict:
        """
        ? Deletes an element from the repository.
        """
        pass
