from IPython.core.magic import register_cell_magic
from IPython.display import display, HTML
from IPython.display import Markdown as md


def make_checker_magic(name):
    """Decorator to turn a function into a cell magic that handles errors."""
    def decorator(handler_func):
        @register_cell_magic(name)
        def magic(line, cell):
            try:
                exec(cell, globals())
                handler_func([globals(), cell])
            except Exception as e:
                handler_func(e)
        return handler_func
    return decorator
