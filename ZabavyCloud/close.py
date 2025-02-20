from .utils.time_utils import duration


class Close:
    def __call__(self, context: any):
        start_time: float = context.application.start
        duration_time: float = round(duration(start=start_time), 2)
        context.logging.info(f"Execution time: {duration_time} s.")
