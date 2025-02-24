import reflex as rx

from ..constants.route import Route
from ..models.field import FieldModel
from ..models.actuator import ActuatorModel
from ..services.actuator import ActuatorService, build_service
from ..utils.uuid_utils import generate_id


class ActuatorState(rx.State):
    module: str = Route.ACTUATOR.value

    fields: list[FieldModel] = [
        FieldModel(
            name='uid',
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
            name='actions',
            type='text',
            placeholder='Actions',
            icon='square-sigma',
            required=False,
        ),
    ]

    data: list[ActuatorModel] = []

    selected: str = ''

    opened: bool = False

    @rx.event
    def show_form(self):
        self.opened = True

    @rx.event
    def close_form(self):
        self.opened = False
        for i, field in enumerate(self.fields):
            field.default_value = ''
        self.selected = ''

    def get_data(self):
        service: ActuatorService = build_service()
        self.data: list = service.get_actuator()

    def handle_submit(self, data: dict):
        data['actions'] = data['actions'].split(',')
        service: ActuatorService = build_service()
        model = service.factory(**data)
        if self.selected == '':
            service.create_actuator(model=model)
        else:
            service.update_actuator(model=model, record=self.selected)
        self.get_data()
        self.close_form()

    def handle_update(self, element: str):
        data = list(filter(lambda x: x.uid == element, self.data))
        if not len(data):
            return
        data = data[0].dict()
        self.selected = element
        for i, field in enumerate(self.fields):
            field.default_value = data[field.name]
        self.show_form()

    def handle_delete(self, element: str):
        service: ActuatorService = build_service()
        service.delete_actuator(record=element, reason='')
        self.get_data()

    def handle_search(self, text: str):
        if not len(text):
            return self.get_data()
        text = text.lower()
        data = [
            item
            for item in self.data
            if any(text in str(value).lower() for value in item.dict().values())
        ]
        self.data = data
