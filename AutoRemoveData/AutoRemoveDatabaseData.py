from time import localtime

from PyQt5.QtCore import QThread
from pyodbc import connect, Error, OperationalError

from Messages import MessageBox
from String import SQLString


class AutoRemoveDatabaseData(QThread):
    def __init__(self, win, server, username, password, database, remove_cycle):
        super(AutoRemoveDatabaseData, self).__init__()
        self.win = win
        self.server = server
        self.username = username
        self.password = password
        self.database = database
        self.remove_cycle = remove_cycle
        self.db = None
        self.cursor = None
        self.localtime = None

        self.msgBox = MessageBox()
        self.sql_string = SQLString()

    def run(self):
        while True:
            try:
                self.db = connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server +
                    ';DATABASE=' + self.database +
                    ';UID=' + self.username +
                    ';PWD=' + self.password)
                self.cursor = self.db.cursor()
            except (Error, OperationalError):
                self.msgBox.connect_to_db_error_message()
                return 0

            self.localtime = localtime()
            self.cursor.execute(self.sql_string.select_create_table_date)
