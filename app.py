import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QTabWidget, QStyleFactory, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from utils import logger
from view.book_view import BookTab
from view.query_view import QueryTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Management System")
        self.setFixedSize(800, 600)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setTabsClosable(False)
        self.tabs.setMovable(True)
        self.tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #C0C0C0;
                border-radius: 5px;
                background: #F5F5F5;
            }
            QTabBar::tab {
                background: #E0E0E0;
                border: 1px solid #BDBDBD;
                border-radius: 5px;
                padding: 8px 20px;
                margin: 2px;
            }
            QTabBar::tab:selected {
                background: #FFFFFF;
                border-bottom: 2px solid #3F51B5;
                color: #3F51B5;
            }
        """)

        self.setCentralWidget(self.tabs)

        self.book_tab = BookTab()
        self.query_tab = QueryTab()
        self.tabs.addTab(self.book_tab, "📚 Books")
        self.tabs.addTab(self.query_tab, "🔍 Queries")
        self.setFont(QFont("Open Sans", 11))


def main():
    app = QApplication(sys.argv)

    app.setStyle(QStyleFactory.create("Fusion"))

    palette = app.palette()
    palette.setColor(palette.Window, Qt.white)
    palette.setColor(palette.WindowText, Qt.black)
    palette.setColor(palette.Base, Qt.white)
    palette.setColor(palette.AlternateBase, Qt.lightGray)
    palette.setColor(palette.ToolTipBase, Qt.white)
    palette.setColor(palette.ToolTipText, Qt.black)
    palette.setColor(palette.Text, Qt.black)
    palette.setColor(palette.Button, Qt.lightGray)
    palette.setColor(palette.ButtonText, Qt.black)
    app.setPalette(palette)

    try:
        window = MainWindow()
        window.show()

    except Exception as exp:
        logger.critical(f"Cannot lunch the application. Error {str(exp)}")
        QMessageBox.critical(None, "Error", "Fatal error. Check logs for debugging.")
        return

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
