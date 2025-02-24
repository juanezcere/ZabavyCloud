import reflex as rx

from ..constants.route import Route
from ..models.field import FieldModel
from ..models.gateway import GatewayModel
from ..services.gateway import GatewayService, build_service
from ..utils.uuid_utils import generate_id


class GatewayState(rx.State):
    module: str = Route.GATEWAY.value

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
            name='devices',
            type='text',
            placeholder='Devices',
            icon='square-sigma',
            required=False,
        ),
    ]

    data: list[GatewayModel] = []

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
        service: GatewayService = build_service()
        self.data: list = service.get_gateway()

    def handle_submit(self, data: dict):
        data['devices'] = data['devices'].split(',')
        service: GatewayService = build_service()
        model = service.factory(**data)
        if self.selected == '':
            service.create_gateway(model=model)
        else:
            service.update_gateway(model=model, record=self.selected)
        self.get_data()
        self.close_form()

    def handle_update(self, element: str):
        data = list(filter(lambda x: x.id == element, self.data))
        if not len(data):
            return
        data = data[0].dict()
        self.selected = element
        for i, field in enumerate(self.fields):
            field.default_value = data[field.name]
        self.show_form()

    def handle_delete(self, element: str):
        service: GatewayService = build_service()
        service.delete_gateway(record=element, reason='')
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
