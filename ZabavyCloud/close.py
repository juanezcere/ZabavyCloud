from .utils.time_utils import duration


class Close:
    def __call__(self, context: any):
        duration_time: float = round(duration(start=context.app.start), 2)
        context.logging.info(f"Execution time: {duration_time} s.")
