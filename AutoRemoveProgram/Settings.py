from PyQt5.QtCore import QTime, pyqtSlot
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.uic import loadUi

from MessageBox import MessageBox
from String import NameString, PathString


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


class CycleSettings(QDialog):
    def __init__(self, win: QMainWindow):
        super(CycleSettings, self).__init__()
        self.win = win
        self.name_string = NameString()
        self.path_string = PathString()
        self.msgBox = MessageBox()
        loadUi(self.path_string.cycle_settings_ui_path_string, self)

        self.cycle_list = self.read_cycle_list()
        self.update_cycle_list = self.cycle_list
        self.cycle_buf = self.update_cycle_list[1:]
        self.listWidget.addItems(self.cycle_list[1:])

    def read_cycle_list(self):
        with open(self.path_string.cycle_list_path_string, 'r') as f:
            return f.read().splitlines()

    def get_cycle_list(self):
        return self.cycle_list

    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            int(self.lineEdit.text())
        except ValueError:
            self.msgBox.cycle_setting_input_error_message()
        self.cycle_buf.append((str(self.lineEdit.text())))
        self.cycle_buf = list(map(int, self.cycle_buf))
        self.cycle_buf.sort()
        self.update_cycle_list = [self.name_string.time_settings_list_default_text]
        self.update_cycle_list.extend(self.cycle_buf)
        self.update_cycle_list = list(map(str, self.update_cycle_list))
        self.listWidget.clear()
        self.listWidget.addItems(self.update_cycle_list[1:])

    @pyqtSlot()
    def on_buttonBox_accepted(self):
        self.cycle_list = self.update_cycle_list
        self.save_cycle_list()

    @pyqtSlot()
    def on_buttonBox_rejected(self):
        self.update_cycle_list = self.cycle_list
        self.lineEdit.clear()
        self.listWidget.clear()
        self.listWidget.addItems(self.cycle_list[1:])

    def save_cycle_list(self):
        with open(self.path_string.cycle_list_path_string, 'w') as f:
            for each in self.cycle_list:
                f.write(each + '\n')
