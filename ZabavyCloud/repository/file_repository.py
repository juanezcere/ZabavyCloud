import json

from ..constants.collection import Collection
from ..utils.uuid_utils import generate_id
from .repository import Repository


class FileRepository(Repository):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def _get_file_path(self, collection: Collection) -> str:
        """
        ? Obtains the path to the json file indicated by the Collection class.
        """
        file_name = f"{collection.value}.json"  # Nombre del archivo basado en la colección
        return f"{self.base_path}/{file_name}"

    def read(self, collection: Collection, record: str, skip: int = 0, limit: int = 100) -> list:
        file_path = self._get_file_path(collection)
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            return []  # Archivo no encontrado, retorna lista vacía
        except json.JSONDecodeError:
            return []  # Error al decodificar JSON, retorna lista vacía

        resultados = []
        # Evaluar la cadena de filtros (usando la función auxiliar segura)
        for item in data:
            if evaluar_filtro(item, filters):
                resultados.append(item)

        return resultados[skip:skip + limit]

    def create(self, collection: Collection, data: dict) -> dict:
        file_path = self._get_file_path(collection)
        try:
            with open(file_path, 'r') as f:
                all_data = json.load(f)
        except FileNotFoundError:
            all_data = []  # Si el archivo no existe, crea una lista vacía
        except json.JSONDecodeError:
            all_data = []

        new_id = generate_id()
        data['id'] = new_id
        all_data.append(data)

        with open(file_path, 'w') as f:
            json.dump(all_data, f, indent=4)  # Guarda los datos actualizados
        return data

    def update(self, collection: Collection, record: str, data: dict) -> dict:
        file_path = self._get_file_path(collection)
        try:
            with open(file_path, 'r') as f:
                all_data = json.load(f)
        except FileNotFoundError:
            return None  # Archivo no encontrado

        for i, item in enumerate(all_data):
            if str(item.get("id")) == record:  # Compara IDs como strings
                all_data[i].update(data)
                with open(file_path, 'w') as f:
                    json.dump(all_data, f, indent=4)
                return all_data[i]
        return None  # Registro no encontrado

    def delete(self, collection: Collection, record: str, reason: str) -> dict:
        file_path = self._get_file_path(collection)
        try:
            with open(file_path, 'r') as f:
                all_data = json.load(f)
        except FileNotFoundError:
            return None  # Archivo no encontrado

        for i, item in enumerate(all_data):
            if str(item.get("id")) == record:  # Compara IDs como strings
                deleted_data = all_data.pop(i)
                with open(file_path, 'w') as f:
                    json.dump(all_data, f, indent=4)
                return deleted_data
        return None  # Registro no encontrado
