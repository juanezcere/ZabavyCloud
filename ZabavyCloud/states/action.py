import reflex as rx

from ..constants.route import Route
from ..models.field import FieldModel
from ..models.action import ActionModel
from ..services.action import ActionService, build_service
from ..utils.uuid_utils import generate_id


class ActionState(rx.State):
    module: str = Route.ACTION.value

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
    ]

    data: list[ActionModel] = []

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
        service: ActionService = build_service()
        self.data: list = service.get_action()

    def handle_submit(self, data: dict):
        if not self.opened:
            return
        service: ActionService = build_service()
        model = service.factory(**data)
        if self.selected == '':
            service.create_action(model=model)
        else:
            service.update_action(model=model, record=self.selected)
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
        service: ActionService = build_service()
        service.delete_action(record=element, reason='')
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
