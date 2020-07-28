from datetime import datetime
from time import time, localtime

from PyQt5.QtCore import QThread
from pyodbc import connect, Error, OperationalError, ProgrammingError

from Messages import MessageBox, EventLog
from String import SQLString, NameString


class AutoRemoveDatabaseData(QThread):
    def __init__(self, remove_setting_dialog, remove_db_list):
        super(AutoRemoveDatabaseData, self).__init__()
        self.name_string = NameString()
        self.event_log = EventLog()
        self.remove_setting_dialog = remove_setting_dialog
        self.remove_db_list = remove_db_list

        self.db = None
        self.cursor = None
        self.localtime = None
        self.table_create_time = None
        self.remove_tables_list = None

        self.msgBox = MessageBox()
        self.sql_string = SQLString()

    def update_data(self, remove_db_list):
        self.remove_db_list = remove_db_list

    def run(self):
        while True:
            self.localtime = localtime()
            if self.localtime.tm_hour == self.remove_setting_dialog.get_time_value().hour() and \
                    self.localtime.tm_min == self.remove_setting_dialog.get_time_value().minute():
                if self.remove_db_list:
                    for item in self.remove_db_list:
                        if self.connect_db(item[0], item[1], item[2], item[3], item[4]):
                            self.remove_tables(item[0], item[4], item[5])

    def connect_db(self, server, port, username, password, database):
        while True:
            try:
                self.db = connect(
                    'DRIVER={SQL Server};SERVER=' + server +
                    ',' + port +
                    ';DATABASE=' + database +
                    ';UID=' + username +
                    ';PWD=' + password, timeout=1)
                self.cursor = self.db.cursor()
                self.event_log.logger(self.name_string.connect_db_success_log_msg)
                return True

            except (Error, OperationalError):
                self.event_log.logger(self.name_string.connect_db_fail_log_msg)
                reply = self.msgBox.connect_to_db_error_message()
                if reply is not self.msgBox.Retry:

                    return False

    def remove_tables(self, server, database, cycle_time):
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
            if time_lag.days >= int(cycle_time):
                self.cursor.execute(self.sql_string.drop_table + '[' + each_table[0] + '];')
                self.db.commit()
                self.event_log.logger(server + '.' + database + '.' + each_table[0] + ' ' +
                                      self.name_string.remove_data_success_log_msg)
