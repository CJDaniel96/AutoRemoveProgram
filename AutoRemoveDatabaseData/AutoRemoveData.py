from PyQt5.QtCore import QThread
from pyodbc import connect


class AutoRemoveData(QThread):
    def __init__(self, win, server, username, password, database):
        super(AutoRemoveData, self).__init__()
        self.win = win
        self.server = server
        self.username = username
        self.password = password
        self.database = database
        self.db = connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server +
            ';DATABASE=' + self.database +
            ';UID=' + self.username +
            ';PWD=' + self.password)
        self.cursor = self.db.cursor()
