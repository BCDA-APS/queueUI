"""
Defines MainWindow class.

.. autosummary::

    ~MainWindow
"""

from bluesky_queueserver_api.zmq import REManagerAPI
from PyQt5 import QtWidgets

from . import APP_TITLE, utils
from .user_settings import settings

UI_FILE = utils.getUiFileName(__file__)

# Connect to the QServer
# def queueserver_api():
#     try:
#         #Where is the TOML file located?
#         config = load_config()["queueserver"]
#     except KeyError:
#         raise InvalidConfiguration("Could not load queueserver info from iconfig.toml file.")
#     ctrl_addr = f"tcp://{config['control_host']}:{config['control_port']}"
#     info_addr = f"tcp://{config['info_host']}:{config['info_port']}"
#     api = REManagerAPI(zmq_control_addr=ctrl_addr, zmq_info_addr=info_addr)
#     return api


class MainWindow(QtWidgets.QMainWindow):
    """
    The main window of the app, built in Qt designer.

    """

    def __init__(self):
        super().__init__()
        utils.myLoadUi(UI_FILE, baseinstance=self)
        self.setWindowTitle(APP_TITLE)

        # self.actionOpen.triggered.connect(self.doOpen)
        self.actionAbout.triggered.connect(self.doAboutDialog)
        self.actionExit.triggered.connect(self.doClose)

        settings.restoreWindowGeometry(self, "mainwindow_geometry")
        print("Settings are saved in:", settings.fileName())

        self.RM = REManagerAPI()

        self.run_engine_state_change()
        self.REOpenButton.clicked.connect(self.openRunEngine)
        self.RECloseButton.clicked.connect(self.closeRunEngine)

        # Controlling the Run Engine
        self.REPlayButton.clicked.connect(self.RM.re_runs)
        self.REPauseButton.clicked.connect(self.RM.re_pause)
        self.REResumeButton.clicked.connect(self.RM.re_resume)
        self.REStopButton.clicked.connect(self.RM.re_stop)
        self.REAbortButton.clicked.connect(self.RM.re_abort)
        self.REHaltButton.clicked.connect(self.RM.re_halt)

        # Controlling the Queue
        self.queuePlayButton.clicked.connect(self.RM.queue_start)
        self.queueStopButton.clicked.connect(self.RM.queue_stop)
        # self.autoPlayCheckBox.clicked.connect(self.toggled)

        # Labels
        self.REEnvironmentOutputLabel.setStyleSheet("color: green; ")
        self.REEnvironmentOutputLabel.setText("Test")

        # Combobox
        plans = self.RM.plans_allowed()["plans_allowed"].keys()
        self.comboBox.clear()
        self.comboBox.addItems(plans)
        self.comboBox.activated.connect(self.get_plans)

    # RE Function:

    def openRunEngine(self):
        """Open RE"""
        self.RM.environment_open()
        self.RM.wait_for_idle()
        self.run_engine_state_change()

    def closeRunEngine(self):
        """Close RE"""
        self.RM.environment_close()
        self.RM.wait_for_idle()
        self.run_engine_state_change()

    def run_engine_state(self, status, status_string):
        """Set RE State"""
        self.setStatus(f"RE Environment is {status_string}.", timeout=0)
        if status is True:
            self.RECloseButton.setEnabled(True)
            self.REOpenButton.setEnabled(False)
        else:
            self.RECloseButton.setEnabled(False)
            self.REOpenButton.setEnabled(True)

        self.setStatus(f"RE Environment is now {status_string}", timeout=0)

    def run_engine_state_change(self):
        """Check RE state"""
        if self.RM.status().get("worker_environment_exists"):
            status_string = "open"
            self.run_engine_state(True, status_string)
        else:
            status_string = "closed"
            self.run_engine_state(False, status_string)

    def destroyRunEngine(self):
        """Destroys the RunEngine."""
        # TODO: Remove this function.
        self.RM.environment_destroy()

    @property
    def status(self):
        """Returns the current message in the mainwindow status bar.

        Returns:
            str: the current message in the mainwindow status bar.
        """
        return self.statusbar.currentMessage()

    def setStatus(self, text, timeout=0):
        """Write new status to the main window and terminal output."""
        print(text)
        self.statusbar.showMessage(str(text), msecs=timeout)

    def doAboutDialog(self, *args, **kw):
        """
        Show the "About ..." dialog
        """
        from .aboutdialog import AboutDialog

        about = AboutDialog(self)
        about.open()

    def closeEvent(self, event):
        """
        User clicked the big [X] to quit.
        """
        self.doClose()
        event.accept()  # let the window close

    def doClose(self, *args, **kw):
        """
        User chose exit (or quit), or closeEvent() was called.
        """
        self.setStatus("Application quitting ...")
        settings.saveWindowGeometry(self, "mainwindow_geometry")
        self.close()

    # def doOpen(self, *args, **kw):
    #     """
    #     User chose to open (connect with) a queue server.
    #     """
    #     from .opendialog import OpenDialog

    #     self.setStatus("Please select a server...")
    #     open_dialog = OpenDialog(self)

    # def doPopUp(self, message):
    #     """
    #     User chose to open (connect with) a tiled server.
    #     """
    #     from .popup import PopUp

    #     popup = PopUp(self, message)
    #     return popup.exec_() == QtWidgets.QDialog.Accepted

    # def proceed(self):
    #     """Handle the logic when the user clicks 'OK'."""
    #     return True

    # def cancel(self):
    #     """Handle the logic when the user clicks 'Cancel'."""
    #     return False
