class SQLString:
    def __init__(self):
        self.select_create_table_date = 'SELECT * FROM sys.tables;'
        self.drop_table = 'DROP TABLE '
        self.check_table_exist = 'IF EXISTS(SELECT * FROM '
