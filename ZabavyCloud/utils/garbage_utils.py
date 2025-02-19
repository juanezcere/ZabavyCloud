import gc


def collect() -> None:
    """
    ? Collects all garbage to clean the memory.
    """
    gc.collect()
