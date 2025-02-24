import reflex as rx


class FieldModel(rx.Base):
    name: str
    type: str
    placeholder: str
    icon: str
    default_value: str = ''
    size: str = '3'
    min_length: int = 1
    max_length: int = 250
    required: bool = True
    disabled: bool = False
    autocomplete: bool = True
