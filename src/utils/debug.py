""" Debugging utilities module. """


def pyqt_set_trace():
    """Set a tracepoint in the Python debugger that works with Qt."""

    import pdb

    from PyQt5.QtCore import pyqtRemoveInputHook

    from utils.helpers import tr

    pyqtRemoveInputHook()
    print(tr('Using custom debug function...'))

    try:
        import pudb

        pudb.set_trace()
    except ImportError:
        pdb.set_trace()


# Use this environment variable to have breakpoint() call the custom debug function
# export PYTHONBREAKPOINT="kan_imagery_catalog.utils.debug.pyqt_set_trace"
