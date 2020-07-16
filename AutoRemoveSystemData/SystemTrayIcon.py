from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QMainWindow, QDialog

from String import NameString, PathString


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, win: QMainWindow, time_settings: QDialog, cycle_settings: QDialog):
        super(SystemTrayIcon, self).__init__()
        self.win = win
        self.time_settings = time_settings
        self.cycle_settings = cycle_settings
        self.name_string = NameString()
        self.path_string = PathString()

        self.menu = QMenu()
        self.openAction = self.menu.addAction(QIcon(self.path_string.open_icon), self.name_string.menu_open)
        self.timeSettingsAction = self.menu.addAction(QIcon(self.path_string.time_settings_icon),
                                                      self.name_string.menu_time_settings)
        self.cycleSettingsAction = self.menu.addAction(QIcon(self.path_string.cycle_settings_icon),
                                                       self.name_string.menu_cycle_settings)
        self.exitAction = self.menu.addAction(QIcon(self.path_string.exit_icon), self.name_string.menu_exit)

        self.openAction.triggered.connect(self.win.show)
        self.cycleSettingsAction.triggered.connect(self.cycle_settings.show)
        self.timeSettingsAction.triggered.connect(self.time_settings.show)
        self.exitAction.triggered.connect(self.win.on_exit_program_clicked)

        self.setIcon(QIcon(self.path_string.system_tray_icon))
        self.setContextMenu(self.menu)
        self.setToolTip(self.name_string.remove_program_text)
