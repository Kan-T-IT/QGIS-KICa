def pyqt_set_trace():
    import pdb

    from PyQt5.QtCore import pyqtRemoveInputHook

    pyqtRemoveInputHook()
    print(tr('Using custom debug function...'))

    try:
        import pudb

        pudb.set_trace()
    except ImportError:
        pdb.set_trace()


# Use this environment variable to have breakpoint() call the custom debug function
# export PYTHONBREAKPOINT="kan_imagery_catalog.utils.debug.pyqt_set_trace"
