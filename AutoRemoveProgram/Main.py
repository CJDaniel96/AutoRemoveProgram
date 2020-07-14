import sys

from PyQt5.QtWidgets import QApplication

from AutoRemoveProgram.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())