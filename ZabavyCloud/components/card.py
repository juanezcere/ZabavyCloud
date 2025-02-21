import reflex as rx

from .button import Button


def Card(module: str, id: str = '', name: str = 'Name', description: str = 'Description', image: str = 'assets/images/pimedica.png'):
    return rx.card(
        rx.link(
            rx.hstack(
                rx.avatar(
                    rx.icon(tag=image, size=30),
                    fallback=name,
                    size='5',
                    radius='full',
                ),
                rx.separator(orientation='vertical'),
                rx.box(
                    rx.heading(
                        name,
                        weight='bold',
                        size='7',
                        align='left',
                        trim='normal',
                    ),
                    rx.text(
                        description,
                        weight='light',
                        size='3',
                        align='left',
                        trim='normal',
                    ),
                    width='100%',
                ),
                rx.separator(orientation='vertical'),
                rx.hstack(
                    Button(
                        image='pen',
                        tooltip='Edit',
                        event='',
                    ),
                    Button(
                        image='trash',
                        tooltip='Delete',
                        event='',
                        color='red',
                    ),
                ),
                spacing='3',
                align='center',
                justify='center',
                width='100%',
            ),
            href=f'{module}/{id}',
        ),
        variant='surface',
        width='100%',
    )


def CardList(state: any) -> rx.vstack:
    return rx.vstack(
        rx.hstack(
            rx.input(
                rx.input.slot(
                    rx.icon(tag='search'),
                ),
                placeholder='Search here...',
                width='100%',
            ),
            rx.dialog.root(
                rx.dialog.trigger(
                    Button(
                        image='plus',
                        tooltip='Create',
                        event='',
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title('Data creation'),
                    rx.dialog.description('Form to create data.'),
                    rx.vstack(
                        rx.foreach(
                            state.fields,
                            lambda x: rx.vstack(
                                rx.text(x.title),
                                rx.input(
                                    placeholder=x.title,
                                    name=x.id,
                                    type=x.type,
                                    width='100%',
                                ),
                                width='100%',
                                justify='center',
                                spacing='2',
                            )
                        ),
                        spacing='3',
                        margin_top='16px',
                        justify='center',
                    ),
                    rx.flex(
                        rx.dialog.close(
                            Button(
                                image='save',
                                tooltip='Save',
                                event='',
                            )
                        ),
                        rx.dialog.close(
                            Button(
                                image='circle-x',
                                tooltip='Close',
                                event='',
                                color='red',
                            )
                        ),
                        spacing='3',
                        margin_top='16px',
                        justify='end',
                    ),
                ),
            ),
            spacing='5',
            align='center',
        ),
        rx.data_list.root(
            rx.foreach(
                state.data,
                lambda item: rx.data_list.item(
                    Card(
                        module=state.module,
                        id=item.id,
                        name=item.name,
                        description=item.description,
                        image=item.image
                    ),
                    align='center',
                )
            ),
        ),
        width='100%',
        spacing='3',
        align='center',
    )
