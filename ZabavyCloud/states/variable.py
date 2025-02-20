import reflex as rx

from ..services.variable import VariableService, build_service


class VariableState(rx.State):
    columns: list = [
        {"title": "Id", "type": "str"},
        {"title": "Name", "type": "str"},
        {"title": "Image", "type": "str"},
        {"title": "Platform", "type": "str"},
        {"title": "Description", "type": "str"},
        {"title": "Maximum", "type": "float"},
        {"title": "Minimum", "type": "float"},
        {"title": "Offset", "type": "float"},
        {"title": "Equation", "type": "str"},
    ]

    data: list = []

    def click_cell(self, pos):
        col, row = pos
        yield self.get_clicked_data(pos)

    def get_clicked_data(self, pos) -> str:
        self.clicked_data = f"Cell clicked: {pos}"
        print(self.clicked_data)

    def get_data(self):
        service: VariableService = build_service()
        data: list = service.get_variable()
        self.data = [list(record.dict().values()) for record in data]
