from datetime import datetime
from time import time, localtime

from PyQt5.QtCore import QThread
from pyodbc import connect, Error, OperationalError, ProgrammingError

from Messages import MessageBox
from String import SQLString


class AutoRemoveDatabaseData(QThread):
    def __init__(self, win, remove_setting_dialog, server, port, username, password, database):
        super(AutoRemoveDatabaseData, self).__init__()
        self.win = win
        self.remove_setting_dialog = remove_setting_dialog
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.database = database

        self.db = None
        self.cursor = None
        self.localtime = None
        self.table_create_time = None
        self.remove_tables_list = None

        self.msgBox = MessageBox()
        self.sql_string = SQLString()

    def run(self):
        while True:
            self.localtime = localtime()
            if self.localtime.tm_hour == self.remove_setting_dialog.get_time_value().hour() and \
                    self.localtime.tm_min == self.remove_setting_dialog.get_time_value().minute():
                if self.remove_tables_list:
                    if self.connect_db():
                        self.remove_tables()
                        self.finished()

    def update_remove_tables(self, remove_tables_list):
        self.remove_tables_list = remove_tables_list

    def connect_db(self):
        while True:
            try:
                self.db = connect(
                    'DRIVER={SQL Server};SERVER=' + self.server +
                    ',' + self.port +
                    ';DATABASE=' + self.database +
                    ';UID=' + self.username +
                    ';PWD=' + self.password)
                self.cursor = self.db.cursor()

                return True

            except (Error, OperationalError):
                reply = self.msgBox.connect_to_db_error_message()
                if reply is not self.msgBox.Retry:

                    return False

    def remove_tables(self):
        self.localtime = datetime.fromtimestamp(time())
        self.cursor.execute(self.sql_string.select_create_table_date)
        tables = []
        table = self.cursor.fetchone()
        while table:
            tables.append(table)
            table = self.cursor.fetchone()

        for each_table in tables:
            self.table_create_time = each_table[7]
            time_lag = self.localtime - self.table_create_time
            if time_lag.days >= self.remove_cycle:
                try:
                    self.cursor.execute(self.sql_string.drop_table + each_table[0] + ';')
                    self.db.commit()
                except ProgrammingError:
                    reply = self.msgBox.drop_db_table_error_message()
                    if reply is self.msgBox.Ignore:
                        continue
                    else:
                        break
