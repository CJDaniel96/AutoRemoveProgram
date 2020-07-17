from os.path import isfile, isdir

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from numpy import array

from AutoRemoveData import AutoRemoveDatabaseData, AutoRemoveSystemData
from Messages import MessageBox
from String import NameString, PathString
from Settings import TimeSettings, CycleSettings
from Tray import SystemTrayIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.name_string = NameString()
        self.path_string = PathString()
        loadUi(self.path_string.win_ui_path_string, self)

        self.cycle_settings = CycleSettings(self)
        self.time_settings = TimeSettings()
        self.msgBox = MessageBox()

        self.select_date = None
        self.date_setting_box_list = self.cycle_settings.get_cycle_list()
        self.date_setting_box.addItems(self.date_setting_box_list)

        self.remove_item_list = []
        self.read_remove_list()
        self.remove_list_display()
        self.auto_remove_data = AutoRemoveSystemData(self.remove_item_list, self.time_settings)
        self.auto_remove_data.start()

        self.tray = SystemTrayIcon(self, self.time_settings, self.cycle_settings)
        self.tray.show()
        self.tray.activated.connect(self.system_tray_icon_activated)

        self.listWidget.itemDoubleClicked.connect(self.on_listWidget_itemDoubleClicked)

        # DataBase Remove Data
        self.database_select_date = None
        self.database_remove_data = None
        self.database_date_setting_box.addItems(self.date_setting_box_list)

    @pyqtSlot(int)
    def on_date_setting_box_activated(self, index):
        self.select_date = self.date_setting_box_list[index]

    @pyqtSlot()
    def on_auto_remove_button_clicked(self):
        if self.select_date is None or self.select_date == self.name_string.time_settings_list_default_text:
            self.msgBox.date_setting_box_error_message()
        elif isdir(self.lineEdit.text()) is False and isfile(self.lineEdit.text()) is False:
            self.msgBox.lineEdit_error_message()
        else:
            reply = self.msgBox.auto_remove_message()
            if reply == self.msgBox.Save:
                remove_item = [self.lineEdit.text(), str(self.select_date)]
                if self.remove_item_list != [] and remove_item[0] in array(self.remove_item_list)[:, 0]:
                    reply = self.msgBox.remove_path_cover_message()
                    if reply == self.msgBox.Yes:
                        row = self.remove_list_update(remove_item)
                        self.listWidget.takeItem(row)
                        self.listWidget.addItems(
                            [self.lineEdit.text() + '\t' + str(self.select_date) + self.name_string.days_cycle])
                        self.save_remove_list()
                else:
                    self.listWidget.addItems(
                        [self.lineEdit.text() + '\t' + str(self.select_date) + self.name_string.days_cycle])
                    self.remove_item_list.append(remove_item)
                    self.auto_remove_data.update_data(self.remove_item_list)
                    self.save_remove_list()

    @pyqtSlot()
    def on_listWidget_itemDoubleClicked(self):
        reply = self.msgBox.listWidget_click_message()
        if reply == self.msgBox.Yes:
            self.remove_item_list.pop(self.listWidget.currentRow())
            self.save_remove_list()
            self.listWidget.takeItem(self.listWidget.currentRow())

    @pyqtSlot()
    def on_exit_program_clicked(self):
        reply = self.msgBox.exit_program()
        if reply == self.msgBox.Yes:
            self.tray.setVisible(False)
            self.tray.hide()
            QCoreApplication.instance().quit()

    def system_tray_icon_activated(self, reason):
        if reason == self.tray.DoubleClick:
            self.show()

    def remove_list_update(self, remove_item):
        for idx, item in enumerate(self.remove_item_list):
            if remove_item[0] in item[0]:
                self.remove_item_list.pop(idx)
                self.remove_item_list.append(remove_item)

                return idx

    def save_remove_list(self):
        if not self.remove_item_list:
            with open(self.path_string.remove_list_text, 'w') as f:
                f.write('')
        else:
            with open(self.path_string.remove_list_text, 'w') as f:
                for item in self.remove_item_list:
                    f.write(item[0] + '\n')
                    f.write(item[1] + '\n')

    def read_remove_list(self):
        if isfile(self.path_string.remove_list_text):
            with open(self.path_string.remove_list_text, 'r') as f:
                remove_list_txt = f.read().splitlines()
            if remove_list_txt:
                for i in range(0, len(remove_list_txt), 2):
                    self.remove_item_list.append([remove_list_txt[i], remove_list_txt[i + 1]])

    def remove_list_display(self):
        if self.remove_item_list:
            for item in self.remove_item_list:
                self.listWidget.addItems([item[0] + '\t' + item[1] + self.nameString.days_cycle])

    @pyqtSlot(int)
    def on_database_date_setting_box_activated(self, index):
        self.database_select_date = self.date_setting_box_list[index]

    @pyqtSlot()
    def on_auto_remove_table_button_clicked(self):
        if self.database_select_date is None or \
                self.database_select_date == self.name_string.time_settings_list_default_text:
            self.msgBox.date_setting_box_error_message()
        else:
            self.database_remove_data = AutoRemoveDatabaseData(self,
                                                               self.serverLineEdit.text(),
                                                               self.usernameLineEdit.text(),
                                                               self.passwordLineEdit.text(),
                                                               self.databaseLineEdit.text())
            self.database_remove_data.start()
