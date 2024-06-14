"""
Support functions for this demo project.

.. autosummary::

    ~myLoadUi
    ~getUiFileName
    ~reconnect
    ~debug_signal
"""

import pathlib


def myLoadUi(ui_file, baseinstance=None, **kw):
    """
    Load a .ui file for use in building a GUI.

    Wraps `uic.loadUi()` with code that finds our program's
    *resources* directory.

    :see: http://nullege.com/codes/search/PyQt4.uic.loadUi
    :see: http://bitesofcode.blogspot.ca/2011/10/comparison-of-loading-techniques.html

    inspired by:
    http://stackoverflow.com/questions/14892713/how-do-you-load-ui-files-onto-python-classes-with-pyside?lq=1
    """
    from PyQt5 import uic

    from . import UI_DIR

    if isinstance(ui_file, str):
        ui_file = UI_DIR / ui_file

    # print(f"myLoadUi({ui_file=})")
    return uic.loadUi(ui_file, baseinstance=baseinstance, **kw)


def getUiFileName(py_file_name):
    """UI file name matches the Python file, different extension."""
    return f"{pathlib.Path(py_file_name).stem}.ui"


def reconnect(signal, new_slot):
    """
    Disconnects any slots connected to the given signal and then connects the signal to the new_slot.

    Parameters:
        - signal: The signal to disconnect and then reconnect.
        - new_slot: The new slot to connect to the signal.

    Note:
        - this function catches TypeError which occurs if the signal was not connected to any slots.
    """
    try:
        signal.disconnect()
    except TypeError:
        pass
    signal.connect(new_slot)


def debug_signal(*args, **kwargs):
    """Print statement when a signal is emitted."""
    print("\nSignal emitted with args:", args, "and kwargs:", kwargs)
