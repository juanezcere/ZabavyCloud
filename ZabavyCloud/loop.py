from .utils.decorator_utils import eternal
from .utils.garbage_utils import collect


class Loop:
    @eternal
    def __call__(self, context: any) -> None:

        collect()
