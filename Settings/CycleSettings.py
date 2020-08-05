from os.path import abspath

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Messages.MessageBox import MessageBox
from String.NameString import NameString
from String.PathString import PathString


class CycleSettings(QDialog):
    def __init__(self, win):
        super(CycleSettings, self).__init__()
        self.win = win
        self.name_string = NameString()
        self.path_string = PathString()
        self.msgBox = MessageBox()
        loadUi(abspath(self.path_string.cycle_settings_ui_path_string), self)

        self.cycle_list = self.read_cycle_list()
        self.update_cycle_list = self.cycle_list
        self.cycle_buf = self.update_cycle_list[1:]
        self.listWidget.addItems(self.cycle_list[1:])

        self.listWidget.itemDoubleClicked.connect(self.on_listWidget_itemDoubleClicked)

    def read_cycle_list(self):
        with open(abspath(self.path_string.cycle_list_path_string), 'r', encoding='utf-8') as f:
            return f.read().splitlines()

    def get_cycle_list(self):
        return self.cycle_list

    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            int(self.lineEdit.text())
        except ValueError:
            self.msgBox.cycle_setting_input_error_message()
            return 0
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
        self.win.date_setting_box_list = self.cycle_list
        self.win.date_setting_box.clear()
        self.win.date_setting_box.addItems(self.win.date_setting_box_list)
        self.save_cycle_list()

    @pyqtSlot()
    def on_buttonBox_rejected(self):
        self.update_cycle_list = self.cycle_list
        self.lineEdit.clear()
        self.listWidget.clear()
        self.listWidget.addItems(self.cycle_list[1:])

    @pyqtSlot()
    def on_listWidget_itemDoubleClicked(self):
        reply = self.msgBox.listWidget_click_message()
        if reply == self.msgBox.Yes:
            self.update_cycle_list.pop(self.listWidget.currentRow() + 1)
            self.cycle_list = self.update_cycle_list
            self.listWidget.takeItem(self.listWidget.currentRow())

    def save_cycle_list(self):
        with open(abspath(self.path_string.cycle_list_path_string), 'w') as f:
            for each in self.cycle_list:
                f.write(each + '\n')
