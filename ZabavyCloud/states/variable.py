import reflex as rx

from ..constants.route import Route
from ..models.field import FieldModel
from ..models.variable import VariableModel
from ..services.variable import VariableService, build_service
from ..utils.uuid_utils import generate_id


class VariableState(rx.State):
    module: str = Route.VARIABLE.value

    fields: list[FieldModel] = [
        FieldModel(
            name='id',
            type='text',
            placeholder='Id',
            icon='id-card',
            required=False,
        ),
        FieldModel(
            name='name',
            type='text',
            placeholder='Name',
            icon='square-pen',
        ),
        FieldModel(
            name='image',
            type='text',
            placeholder='Image',
            icon='file-image',
        ),
        FieldModel(
            name='platform',
            type='text',
            placeholder='Platform',
            icon='case-sensitive',
        ),
        FieldModel(
            name='description',
            type='text',
            placeholder='Description',
            icon='scroll-text',
        ),
        FieldModel(
            name='maximum',
            type='number',
            placeholder='Maximum',
            icon='square-plus',
            required=False,
        ),
        FieldModel(
            name='minimum',
            type='number',
            placeholder='Minimum',
            icon='square-minus',
            required=False,
        ),
        FieldModel(
            name='offset',
            type='number',
            placeholder='Offset',
            icon='square-percent',
            required=False,
        ),
        FieldModel(
            name='equation',
            type='text',
            placeholder='Equation',
            icon='square-sigma',
            required=False,
        ),
    ]

    data: list[VariableModel] = []

    selected: str = ''

    opened: bool = False

    @rx.event
    def open_form(self):
        self.opened = True

    @rx.event
    def close_form(self):
        self.opened = False

    def get_data(self):
        service: VariableService = build_service()
        self.data: list = service.get_variable()
        print("Gotten data:", self.data)

    def handle_submit(self, data: dict):
        data['equation'] = data['equation'].split(',')
        service: VariableService = build_service()
        model = service.factory(**data)
        print("Selected:", self.selected)
        if self.selected == '':
            service.create_variable(model=model)
            print("Created")
        else:
            service.update_variable(model=model, record=self.selected)
            print("Updated")
        self.get_data()
        self.close_form()

    def handle_update(self, element: str):
        print("UPDATING")
        self.selected = element
        self.open_form()
        print(self.selected)

    def handle_delete(self, element: str):
        print("DELETING")
        self.selected = element
        print(self.selected)
