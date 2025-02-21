import reflex as rx

from ..constants.route import Route
from ..models.variable import VariableModel
from ..services.variable import VariableService, build_service


class Field(rx.Base):
    id: str
    type: str
    title: str


class VariableState(rx.State):
    module: str = Route.VARIABLE.value

    fields: list[Field] = [
        Field(id='id', type='text', title='Id'),
        Field(id='name', type='text', title='Name'),
        Field(id='image', type='text', title='Image'),
        Field(id='platform', type='text', title='Platform'),
        Field(id='description', type='text', title='Description'),
        Field(id='maximum', type='number', title='Maximum'),
        Field(id='minimum', type='number', title='Minimum'),
        Field(id='offset', type='number', title='Offset'),
        Field(id='equation', type='text', title='Equation'),
    ]

    data: list[VariableModel] = []

    def get_data(self):
        service: VariableService = build_service()
        self.data: list = service.get_variable()
