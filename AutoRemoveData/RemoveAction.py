from os import mkdir
from os.path import isfile, abspath

from String import PathString, NameString


class RemoveListAction:
    def __init__(self):
        self.path_string = PathString()
        self.name_string = NameString()

    @staticmethod
    def remove_list_update(remove_item_list, remove_item):
        for idx, item in enumerate(remove_item_list):
            if remove_item[0] in item[0]:
                remove_item_list.pop(idx)
                remove_item_list.append(remove_item)

                return idx

    def save_remove_list(self, remove_item_list):
        with open(abspath(self.path_string.remove_list_text), 'w') as f:
            if not remove_item_list:
                f.write('')
            else:
                for item in remove_item_list:
                    for each in item:
                        f.write(each + '\n')

    def read_remove_list(self):
        remove_item_list = []
        if isfile(abspath(self.path_string.remove_list_text)):
            with open(abspath(self.path_string.remove_list_text), 'r') as f:
                remove_list_txt = f.read().splitlines()
            if remove_list_txt:
                for i in range(0, len(remove_list_txt), 2):
                    remove_item_list.append([remove_list_txt[i], remove_list_txt[i + 1]])

                return remove_item_list
            else:
                return []
        else:
            with open(abspath(self.path_string.remove_list_text), 'w') as f:
                f.write('')

            return []

    def remove_list_display(self, remove_item_list, listWidget):
        if remove_item_list:
            for item in remove_item_list:
                listWidget.addItem('%-60s %4s %s' % (item[0], item[1], self.name_string.days_cycle))


class RemoveDatabaseAction:
    def __init__(self):
        self.name_string = NameString()
        self.path_string = PathString()

    @staticmethod
    def remove_list_update(remove_db_list, remove_item):
        for idx, item in enumerate(remove_db_list):
            if remove_item[0] in item[0] and remove_item[4] in item[4]:
                remove_db_list.pop(idx)
                remove_db_list.append(remove_item)

                return idx

    def save_remove_list(self, remove_db_list):
        with open(abspath(self.path_string.remove_db_text), 'w') as f:
            if not remove_db_list:
                f.write('')
            else:
                for item in remove_db_list:
                    for each in item:
                        f.write(each + '\n')

    def read_remove_list(self):
        remove_db_list = []
        if isfile(abspath(self.path_string.remove_db_text)):
            with open(abspath(self.path_string.remove_db_text), 'r') as f:
                remove_list_txt = f.read().splitlines()
            if remove_list_txt:
                for i in range(0, len(remove_list_txt), 6):
                    remove_db_list.append([remove_list_txt[i],
                                           remove_list_txt[i + 1],
                                           remove_list_txt[i + 2],
                                           remove_list_txt[i + 3],
                                           remove_list_txt[i + 4],
                                           remove_list_txt[i + 5]])

                return remove_db_list
            else:
                return []
        else:
            with open(abspath(self.path_string.remove_db_text), 'w') as f:
                f.write('')

            return []

    def remove_list_display(self, remove_db_list, table_listWidget):
        if remove_db_list:
            for item in remove_db_list:
                table_listWidget.addItems([item[0] + '.' + item[4] + '\t' + item[5] + self.name_string.days_cycle])
