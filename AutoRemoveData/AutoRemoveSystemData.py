from datetime import datetime
from os import remove, listdir
from os.path import getmtime, isfile, isdir, join
from shutil import rmtree
from time import localtime

from PyQt5.QtCore import QThread

from Messages import EventLog
from String import NameString


class AutoRemoveSystemData(QThread):
    def __init__(self, remove_item_list, remove_setting_dialog):
        super(AutoRemoveSystemData, self).__init__()
        self.name_string = NameString()
        self.localtime = None
        self.permission_error_list = []
        self.remove_item_list = remove_item_list
        self.remove_setting_dialog = remove_setting_dialog
        self.event_log = EventLog()

    def update_data(self, remove_item_list):
        self.remove_item_list = remove_item_list

    def run(self):
        while True:
            self.localtime = localtime()
            if self.localtime.tm_hour == self.remove_setting_dialog.get_time_value().hour() and \
                    self.localtime.tm_min == self.remove_setting_dialog.get_time_value().minute():
                if self.remove_item_list:
                    self.remove_data()

    def remove_data(self):
        for item in self.remove_item_list:
            if isfile(item[0]):
                self.remove_file(item)
            elif isdir(item[0]):
                self.remove_dir(item)

    def remove_file(self, file_item):
        file_time = localtime(getmtime(file_item[0]))
        interval = datetime(self.localtime.tm_year, self.localtime.tm_mon, self.localtime.tm_mday) - datetime(
            file_time.tm_year, file_time.tm_mon, file_time.tm_mday)
        if interval.days >= int(file_item[1]):
            try:
                remove(file_item[0])
                self.event_log.logger(file_item[0] + ' ' + self.name_string.remove_data_success_log_msg)
            except PermissionError:
                if file_item[0] not in self.permission_error_list:
                    self.permission_error_list.append(file_item[0])
                    self.event_log.logger(file_item[0] + ' ' + self.name_string.permission_error_log_msg)

    def remove_dir(self, dir_item):
        files_list = []
        for files in listdir(dir_item[0]):
            full_path = join(dir_item[0], files)
            files_list.extend([full_path])
        for each in files_list:
            each_file_time = localtime(getmtime(each))
            interval = datetime(self.localtime.tm_year, self.localtime.tm_mon, self.localtime.tm_mday) - datetime(
                each_file_time.tm_year, each_file_time.tm_mon, each_file_time.tm_mday)
            if interval.days >= int(dir_item[1]):
                try:
                    rmtree(each)
                    self.event_log.logger(each + ' ' + self.name_string.remove_data_success_log_msg)
                except PermissionError:
                    if each not in self.permission_error_list:
                        self.permission_error_list.append(each)
                        self.event_log.logger(each + ' ' + self.name_string.permission_error_log_msg)
