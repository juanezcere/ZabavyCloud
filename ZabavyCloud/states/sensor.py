import reflex as rx

from ..services.sensor import SensorService, build_service


class SensorState(rx.State):
    columns: list = [
        {"title": "Id", "type": "str"},
        {"title": "Name", "type": "str"},
        {"title": "Image", "type": "str"},
        {"title": "Platform", "type": "str"},
        {"title": "Description", "type": "str"},
        {"title": "Variables", "type": "float"},
    ]

    data: list = []

    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)

    def get_clicked_data(self, pos) -> str:
        self.clicked_data = f"Cell clicked: {pos}"
        print(self.clicked_data)

    def get_data(self):
        service: SensorService = build_service()
        data: list = service.get_sensor()
        self.data = [list(record.dict().values()) for record in data]
