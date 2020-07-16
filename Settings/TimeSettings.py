from PyQt5.QtCore import QTime, pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from String.NameString import NameString
from String.PathString import PathString


class TimeSettings(QDialog):
    def __init__(self):
        super(TimeSettings, self).__init__()
        self.name_string = NameString()
        self.path_string = PathString()
        loadUi(self.path_string.time_settings_ui_path_string, self)

        self.remove_time = QTime()
        self.remove_time.setHMS(9, 0, 0)
        self.timeEdit.setTime(self.remove_time)

    @pyqtSlot()
    def on_buttonBox_accepted(self):
        self.remove_time = self.timeEdit.time()

    def get_time_value(self):
        return self.remove_time
