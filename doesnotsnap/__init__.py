#!/usr/bin/env python3

import sys
import typing
from PyQt5 import (
    QtNetwork,
    QtWidgets,
)


class MainWindow(QtWidgets.QMainWindow):
    pass


class Application(QtWidgets.QApplication):
    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)
        self.manager = QtNetwork.QNetworkAccessManager()
        self.window = MainWindow()

    def run(self):
        self.window.show()
        res = self.exec_()
        self.exit()
        return res


def main():
    app = Application(sys.argv)
    sys.exit(app.run())


if __name__ == "__main__":
    main()
