from os.path import isfile, isdir, abspath

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QFileDialog, QListWidgetItem
from PyQt5.uic import loadUi
from numpy import array

from AutoRemoveData import AutoRemoveDatabaseData, AutoRemoveSystemData, RemoveListAction
from AutoRemoveData.RemoveAction import RemoveDatabaseAction
from Messages import MessageBox
from String import NameString, PathString
from Settings import TimeSettings, CycleSettings
from Tray import SystemTrayIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.name_string = NameString()
        self.path_string = PathString()
        loadUi(abspath(self.path_string.win_ui_path_string), self)

        self.cycle_settings = CycleSettings(self)
        self.time_settings = TimeSettings()
        self.msgBox = MessageBox()

        self.file_path = QFileDialog()
        self.select_date = None
        self.date_setting_box_list = self.cycle_settings.get_cycle_list()
        self.date_setting_box.addItems(self.date_setting_box_list)

        self.remove_item_list = []
        self.remove_list_action = RemoveListAction()
        self.remove_item_list = self.remove_list_action.read_remove_list()
        self.remove_list_action.remove_list_display(self.remove_item_list, self.listWidget)

        self.auto_remove_data = AutoRemoveSystemData(self.remove_item_list, self.time_settings)
        self.auto_remove_data.start()

        self.tray = SystemTrayIcon(self, self.time_settings, self.cycle_settings)
        self.tray.show()
        self.tray.activated.connect(self.system_tray_icon_activated)

        self.font = QFont('Monospace')
        self.font.setStyleHint(QFont.TypeWriter)
        self.listWidget.setFont(self.font)
        self.listWidget.itemDoubleClicked.connect(self.on_listWidget_itemDoubleClicked)

        # DataBase Remove Data
        self.database_select_date = None
        self.database_date_setting_box.addItems(self.date_setting_box_list)

        self.portLineEdit.setText('1433')
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.remove_db_list = []
        self.remove_db_action = RemoveDatabaseAction()
        self.remove_db_list = self.remove_db_action.read_remove_list()
        self.remove_db_action.remove_list_display(self.remove_db_list, self.table_listWidget)

        self.database_remove_data = AutoRemoveDatabaseData(self.time_settings, self.remove_db_list)
        self.database_remove_data.start()

        self.table_listWidget.setFont(self.font)
        self.table_listWidget.itemDoubleClicked.connect(self.on_table_listWidget_itemDoubleClicked)

    @pyqtSlot()
    def on_file_select_clicked(self):
        file_path_text = self.file_path.getOpenFileName(self)
        self.lineEdit.setText(file_path_text[0])

    @pyqtSlot()
    def on_dir_select_clicked(self):
        dir_path_text = self.file_path.getExistingDirectory(self)
        self.lineEdit.setText(dir_path_text)

    @pyqtSlot(int)
    def on_date_setting_box_activated(self, index):
        self.select_date = self.date_setting_box_list[index]

    @pyqtSlot()
    def on_auto_remove_button_clicked(self):
        if self.select_date is None or self.select_date == self.name_string.time_settings_list_default_text:
            self.msgBox.date_setting_box_error_message()
        elif isdir(self.lineEdit.text()) is False and isfile(self.lineEdit.text()) is False:
            self.msgBox.lineEdit_error_message()
        elif self.remove_list_action.remove_rules(self.lineEdit.text()):
            self.msgBox.lineEdit_error_message()
        else:
            reply = self.msgBox.auto_remove_message()
            if reply == self.msgBox.Save:
                remove_item = [self.lineEdit.text(), str(self.select_date)]
                if self.remove_item_list != [] and remove_item[0] in array(self.remove_item_list)[:, 0]:
                    reply = self.msgBox.remove_path_cover_message()
                    if reply == self.msgBox.Yes:
                        row = self.remove_list_action.remove_list_update(self.remove_item_list, remove_item)
                        self.listWidget.takeItem(row)
                        self.listWidget.addItems(
                            ['%-60s %4s %s' % (self.lineEdit.text(), str(self.select_date), self.name_string.days_cycle)])
                        self.remove_list_action.save_remove_list(self.remove_item_list)
                else:
                    self.listWidget.addItems(
                        ['%-60s %4s %s' % (self.lineEdit.text(), str(self.select_date), self.name_string.days_cycle)])
                    self.remove_item_list.append(remove_item)
                    self.auto_remove_data.update_data(self.remove_item_list)
                    self.remove_list_action.save_remove_list(self.remove_item_list)

    @pyqtSlot()
    def on_listWidget_itemDoubleClicked(self):
        reply = self.msgBox.listWidget_click_message()
        if reply == self.msgBox.Yes:
            self.remove_item_list.pop(self.listWidget.currentRow())
            self.remove_list_action.save_remove_list(self.remove_item_list)
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

    @pyqtSlot(int)
    def on_database_date_setting_box_activated(self, index):
        self.database_select_date = self.date_setting_box_list[index]

    @pyqtSlot()
    def on_auto_remove_table_button_clicked(self):
        if self.database_select_date is None or \
                self.database_select_date == self.name_string.time_settings_list_default_text:
            self.msgBox.input_none_error_message()
        else:
            reply = self.msgBox.auto_remove_message()
            if reply == self.msgBox.Save:
                remove_item = [self.serverLineEdit.text(),
                               self.portLineEdit.text(),
                               self.usernameLineEdit.text(),
                               self.passwordLineEdit.text(),
                               self.databaseLineEdit.text(),
                               self.database_select_date]
                if self.remove_db_list != [] and remove_item[0] in array(self.remove_db_list)[:, 0] and \
                        remove_item[4] in array(self.remove_db_list)[:, 4]:
                    reply = self.msgBox.remove_path_cover_message()
                    if reply == self.msgBox.Yes:
                        if self.connect_db_test():
                            row = self.remove_db_action.remove_list_update(self.remove_db_list, remove_item)
                            self.table_listWidget.takeItem(row)
                            self.table_listWidget.addItems([self.serverLineEdit.text() +
                                                            '.' + self.databaseLineEdit.text() +
                                                            '%12s' % self.database_select_date +
                                                            self.name_string.days_cycle])
                            self.remove_db_action.save_remove_list(self.remove_db_list)

                else:
                    if self.connect_db_test():
                        self.table_listWidget.addItems([self.serverLineEdit.text() +
                                                        '.' + self.databaseLineEdit.text() +
                                                        '%12s' % self.database_select_date +
                                                        self.name_string.days_cycle])
                        self.remove_db_list.append(remove_item)
                        self.database_remove_data.update_data(self.remove_db_list)
                        self.remove_db_action.save_remove_list(self.remove_db_list)

    @pyqtSlot()
    def on_table_listWidget_itemDoubleClicked(self):
        reply = self.msgBox.listWidget_click_message()
        if reply == self.msgBox.Yes:
            self.remove_db_list.pop(self.table_listWidget.currentRow())
            self.remove_db_action.save_remove_list(self.remove_db_list)
            self.table_listWidget.takeItem(self.table_listWidget.currentRow())

    def connect_db_test(self):
        if self.database_remove_data.connect_db(self.serverLineEdit.text(),
                                                self.portLineEdit.text(),
                                                self.usernameLineEdit.text(),
                                                self.passwordLineEdit.text(),
                                                self.databaseLineEdit.text()):
            self.database_remove_data.disconnect_db()

            return True

        else:
            return False
