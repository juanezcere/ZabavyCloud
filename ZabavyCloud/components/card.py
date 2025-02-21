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


def Row(module: str, item: any):
    return rx.data_list.item(
        Card(
            module=module,
            id=item.id,
            name=item.name,
            description=item.description,
            image=item.image
        ),
        align='center',
    )


def CardList(data: list, module: str) -> rx.vstack:
    return rx.vstack(
        rx.hstack(
            rx.input(
                rx.input.slot(
                    rx.icon(tag='search'),
                ),
                placeholder='Search here...',
                width='100%',
            ),
            Button(
                image='plus',
                tooltip='create',
                event='',
            ),
            spacing='5',
            align='center',
        ),
        rx.data_list.root(
            rx.foreach(data, lambda x: Row(module=module, item=x)),
        ),
        width='100%',
        spacing='3',
        align='center',
    )
