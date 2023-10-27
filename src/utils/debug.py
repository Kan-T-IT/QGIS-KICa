def pyqt_set_trace():
    import pdb

    from PyQt5.QtCore import pyqtRemoveInputHook

    pyqtRemoveInputHook()
    print("Utilizando la función de debug personalizada...")

    try:
        import pudb

        pudb.set_trace()
    except ImportError:
        pdb.set_trace()


# Usar esta variable de entorno para que breakpoint() llame a la función personalizada de debug
# export PYTHONBREAKPOINT="kan_imagery_catalog.utils.debug.pyqt_set_trace"
