#!/usr/bin/env python3

import sys
import typing
from PyQt5 import (
    QtCore,
    QtNetwork,
    QtWidgets,
)
from PyQt5.QtCore import (
    PYQT_VERSION_STR as pyqt_version,
    qVersion,
)

class MainWindow(QtWidgets.QMainWindow):
    pass


class Application(QtWidgets.QApplication):
    def __init__(self, argv: typing.List[str]) -> None:
        print("PyQt %s" % pyqt_version)
        print("Qt %s" % qVersion())
        super().__init__(argv)
        print("Application: Before QNetworkAccessManager")
        self.manager = QtNetwork.QNetworkAccessManager(self)
        print("Application: After QNetworkAccessManager")
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
