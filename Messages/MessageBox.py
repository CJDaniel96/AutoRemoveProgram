from PyQt5.QtWidgets import QMessageBox

from String import NameString


class MessageBox(QMessageBox):
    """
    The UI MessageBox
    """
    def __init__(self):
        super(MessageBox, self).__init__()
        self.name_string = NameString()

    def auto_remove_message(self):
        self.setIcon(self.Question)
        self.setWindowTitle(self.name_string.question)
        self.setText(self.name_string.auto_remove_message_text)
        self.setInformativeText(self.name_string.auto_remove_message_informativeText)
        self.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        self.setDefaultButton(QMessageBox.Save)
        reply = self.exec_()

        return reply

    def exit_program(self):
        self.setIcon(self.Question)
        self.setWindowTitle(self.name_string.question)
        self.setText(self.name_string.exit_program_text)
        self.setInformativeText(self.name_string.exit_program_informativeText)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        reply = self.exec_()

        return reply

    def date_setting_box_error_message(self):
        self.setIcon(self.Critical)
        self.setWindowTitle(self.name_string.error)
        self.setText(self.name_string.error_file_path)
        self.setInformativeText('')
        self.setStandardButtons(QMessageBox.Retry)
        self.setDefaultButton(QMessageBox.Retry)
        self.exec_()

    def lineEdit_error_message(self):
        self.setIcon(self.Critical)
        self.setWindowTitle(self.name_string.error)
        self.setText(self.name_string.error_file_path)
        self.setInformativeText('')
        self.setStandardButtons(QMessageBox.Retry)
        self.setDefaultButton(QMessageBox.Retry)
        self.exec_()

    def listWidget_click_message(self):
        self.setIcon(self.Question)
        self.setWindowTitle(self.name_string.question)
        self.setText(self.name_string.listWidget_click_message_text)
        self.setInformativeText(self.name_string.listWidget_click_message_informativeText)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        reply = self.exec_()

        return reply

    def remove_path_cover_message(self):
        self.setIcon(self.Warning)
        self.setWindowTitle(self.name_string.warning)
        self.setText(self.name_string.remove_item_cover_text)
        self.setInformativeText('')
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        reply = self.exec_()

        return reply

    def cycle_setting_input_error_message(self):
        self.setIcon(self.Critical)
        self.setWindowTitle(self.name_string.error)
        self.setWindowTitle(self.name_string.error)
        self.setText(self.name_string.cycle_settings_error_input_text)
        self.setInformativeText('')
        self.setStandardButtons(QMessageBox.Retry)
        self.setDefaultButton(QMessageBox.Retry)
        self.exec_()

    def connect_to_db_error_message(self):
        self.setIcon(self.Critical)
        self.setWindowTitle(self.name_string.error)
        self.setText(self.name_string.connect_db_error_text)
        self.setInformativeText('')
        self.setStandardButtons(self.Retry | self.Cancel)
        self.setDefaultButton(self.Retry)
        reply = self.exec_()

        return reply

    def drop_db_table_error_message(self):
        self.setIcon(self.Critical)
        self.setWindowTitle(self.name_string.error)
        self.setText(self.name_string.db_table_programming_error_text)
        self.setInformativeText('')
        self.setStandardButtons(QMessageBox.Ignore | QMessageBox.Discard)
        self.setDefaultButton(QMessageBox.Discard)
        reply = self.exec_()

        return reply

    def input_none_error_message(self):
        self.setIcon(self.Warning)
        self.setWindowTitle(self.name_string.warning)
        self.setText(self.name_string.input_none_error_text)
        self.setInformativeText('')
        self.setStandardButtons(QMessageBox.Close)
        self.setDefaultButton(QMessageBox.Close)
        self.exec_()
