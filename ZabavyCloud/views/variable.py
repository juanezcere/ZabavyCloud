import reflex as rx

from ..components.table import Table
from ..states.variable import VariableState


def VariableView(state: VariableState):
    return Table(
        columns=state.columns,
        data=state.data,
        on_cell_clicked=state.click_cell,
    )
