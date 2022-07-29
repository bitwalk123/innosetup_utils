import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)


class ISUtility(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle('utility for Inno Setup Compiler')

    def init_ui(self):
        pass


def main():
    app = QApplication(sys.argv)
    win = ISUtility()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
