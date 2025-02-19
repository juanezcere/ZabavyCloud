from .uuid_utils import generate_id


class Repository:
    def __init__(self):
        self.data: list = []

    def get(self, record: str = '', skip: int = 0, limit: int = 100) -> list:
        if len(record):
            return list(filter(lambda x: x['id'] == record, self.data))
        return self.data[skip:skip+limit] if skip+limit > len(self.data) else self.data

    def create(self, model: any) -> dict:
        data = model.dict()
        data['id'] = generate_id()
        self.data.append(data)
        return data

    def update(self, model: any, record: str) -> dict:
        data = self.get(record=record)
        if not len(data):
            raise "Not found."
        data = data[0]
        self.data.remove(data)
        data = {**model.dict(), 'id': data['id']}
        self.data.append(data)
        return data

    def delete(self, record: str, reason: str) -> dict:
        data = self.get(record=record)
        if not len(data):
            raise "Not found."
        data = data[0]
        self.data.remove(data)
        return data
