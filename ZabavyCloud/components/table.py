import reflex as rx


def Table(columns: list, data: list, on_cell_clicked: any) -> rx.data_editor:
    return rx.data_editor(
        columns=columns,
        data=data,
        on_cell_clicked=on_cell_clicked,
        row_height=80,
        smooth_scroll_x=True,
        smooth_scroll_y=True,
        column_select='single',
        # theme=DataEditorTheme(**dark_theme),
        height='30vh',
    )
