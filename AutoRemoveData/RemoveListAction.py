from os.path import isfile

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
        if not remove_item_list:
            with open(self.path_string.remove_list_text, 'w') as f:
                f.write('')
        else:
            with open(self.path_string.remove_list_text, 'w') as f:
                for item in remove_item_list:
                    f.write(item[0] + '\n')
                    f.write(item[1] + '\n')

    @property
    def read_remove_list(self):
        remove_item_list = []
        if isfile(self.path_string.remove_list_text):
            with open(self.path_string.remove_list_text, 'r') as f:
                remove_list_txt = f.read().splitlines()
            if remove_list_txt:
                for i in range(0, len(remove_list_txt), 2):
                    remove_item_list.append([remove_list_txt[i], remove_list_txt[i + 1]])

                return remove_item_list
            else:
                return []

    def remove_list_display(self, remove_item_list, listWidget):
        if remove_item_list:
            for item in remove_item_list:
                listWidget.addItems([item[0] + '\t' + item[1] + self.name_string.days_cycle])
