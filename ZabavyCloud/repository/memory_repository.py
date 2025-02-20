from ..constants.collection import Collection
from ..utils.uuid_utils import generate_id
from .repository import Repository


class MemoryRepository(Repository):
    """
    Memory repository implementation based on python dicts.
    """

    def __init__(self):
        self.__data = {}

    def get(self, collection: Collection, filters: str, skip: int = 0, limit: int = 100) -> list:
        if collection not in self.__data:
            return []

        results = []
        # Evaluar la cadena de filtros (esto es un ejemplo muy básico, necesitarás algo más robusto)
        try:
            # CUIDADO: eval() puede ser peligroso.
            eval_filter = eval(filters, {}, self.__data[collection])
        except Exception as e:  # Captura cualquier error de evaluación
            print(f"Error al evaluar el filtro: {e}")
            return []  # En caso de error, retorna una lista vacía.

        for item_id, item_data in self.__data[collection].items():
            if eval_filter(item_data):  # Llama a la función filtro_evaluado
                results.append(item_data)

        return results[skip:skip + limit]

    def post(self, collection: Collection, data: dict) -> dict:
        if collection not in self.__data:
            self.__data[collection] = {}

        if not data:
            raise ValueError(
                "Los datos no pueden estar vacíos para crear un nuevo elemento.")

        new_id = generate_id()
        data['id'] = new_id
        self.__data[collection][new_id] = data
        return data

    def put(self, collection: Collection, register: str, data: dict) -> dict:
        if collection not in self.__data:
            return None

        if register not in self.__data[collection]:
            return None

        self.__data[collection][register].update(data)
        return self.__data[collection][register]

    def delete(self, collection: Collection, register: str, reason: str) -> dict:
        if collection not in self.__data:
            return None

        if register not in self.__data[collection]:
            return None

        deleted_data = self.__data[collection].pop(register)
        return deleted_data
