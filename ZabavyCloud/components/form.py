import reflex as rx

from .button import Button
from ..models.field import FieldModel


def Field(item: FieldModel) -> rx.input:
    return rx.input(
        rx.input.slot(
            rx.icon(tag=item.icon),
        ),
        placeholder=item.placeholder,
        name=item.name,
        type=item.type,
        default_value=item.default_value,
        size=item.size,
        min_length=item.min_length,
        max_length=item.max_length,
        required=item.required,
        disabled=item.disabled,
        variant='classic',
        radius='full',
        width='100%',
    ),


def Form(state: any) -> rx.form:
    return rx.form(
        rx.foreach(
            state.fields,
            lambda x: rx.vstack(
                rx.text(x.placeholder),
                Field(item=x),
                justify='center',
                spacing='2',
                margin='16px'
            )
        ),
        rx.flex(
            rx.form.submit(
                Button(
                    image='save',
                    tooltip='Save',
                    event=None,
                ),
            ),
            Button(
                image='circle-x',
                tooltip='Close',
                event=state.close_form,
                color='red',
            ),
            spacing='3',
            justify='end',
        ),
        margin_y='16px',
        reset_on_submit=True,
        on_submit=state.handle_submit,
    ),
