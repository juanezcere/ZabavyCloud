import reflex as rx

from ..models.variable import VariableModel
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

    data: list[VariableModel] = []

    def get_data(self):
        service: VariableService = build_service()
        self.data: list = service.get_variable()
