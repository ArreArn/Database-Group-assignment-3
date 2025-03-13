from enum import Enum
from typing import List, Dict

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton,
    QTableWidget, QFormLayout, QLabel, QLineEdit, QMessageBox, QTableWidgetItem
)

from controller import QueryController
from utils import logger


class QueryIndex(Enum):
    FIND_BOOKS_BY_AUTHOR = 0
    LIST_ALL_PUBLISHERS = 1
    LIST_ALL_MEMBERS = 2
    LIST_MEMBERS_BY_BOOK = 3
    LIST_MEMBERS_BORROWED_AT_LEAST_ONE_BOOK = 4


QUERY_DESCRIPTIONS: Dict[int, str] = {
    QueryIndex.FIND_BOOKS_BY_AUTHOR.value: "Find all books by a specific author",
    QueryIndex.LIST_ALL_PUBLISHERS.value: "List all publishers",
    QueryIndex.LIST_ALL_MEMBERS.value: "List all members",
    QueryIndex.LIST_MEMBERS_BY_BOOK.value: "List all members who borrowed a particular book",
    QueryIndex.LIST_MEMBERS_BORROWED_AT_LEAST_ONE_BOOK.value: "List all members who borrowed at least one book",
}


class QueryTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.controller = QueryController()
        self.init_ui()

    def init_ui(self) -> None:
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()

        # Combo box for query selection
        self.query_combo = QComboBox()
        self.query_combo.addItems(QUERY_DESCRIPTIONS.values())
        self.query_combo.currentIndexChanged.connect(self.update_form)

        # Execute button
        self.execute_button = QPushButton("Execute")
        self.execute_button.clicked.connect(self.execute_query)

        self.top_layout.addWidget(self.query_combo)
        self.top_layout.addWidget(self.execute_button)

        # Form for input fields
        self.form_layout = QFormLayout()
        self.author_input = QLineEdit()
        self.book_input = QLineEdit()
        self.form_layout.addRow(QLabel("Author:"), self.author_input)
        self.form_layout.addRow(QLabel("Book:"), self.book_input)

        # Table to display results
        self.result_table = QTableWidget()
        self.result_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.result_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.result_table.horizontalHeader().setStretchLastSection(True)

        # Adding layouts
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.result_table)
        self.setLayout(self.main_layout)

        # Styling the UI
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #333;
                font-weight: bold;
            }
            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 6px;
                font-size: 13px;
                background: #f9f9f9;
            }
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 6px;
                background: #ffffff;
            }
            /* Style for the drop-down list of the combo box */
            QComboBox QAbstractItemView {
                background-color: #ffffff;
                border: 1px solid #ccc;
                selection-background-color: #6A0DAD;  /* Dark purple on selection */
                selection-color: white;
            }
            QPushButton {
                background-color: #6A0DAD;  /* Dark purple background */
                color: white;
                border: none;
                border-radius: 0;  /* Flat design with no rounded corners */
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5a009e;  /* Slightly darker purple for hover */
            }
            QTableWidget {
                border: 1px solid #ddd;
                font-size: 13px;
            }
            QTableWidget::item {
                padding: 5px;
            }
        """)

        self.update_form()

    def update_form(self) -> None:
        """Show or hide input fields based on the selected query."""
        selected_index = self.query_combo.currentIndex()
        self.author_input.setVisible(selected_index == QueryIndex.FIND_BOOKS_BY_AUTHOR.value)
        self.book_input.setVisible(selected_index == QueryIndex.LIST_MEMBERS_BY_BOOK.value)

    def execute_query(self) -> None:
        """Execute the selected query and display results."""
        current_index = self.query_combo.currentIndex()
        if current_index == QueryIndex.FIND_BOOKS_BY_AUTHOR.value:
            self.execute_find_books_by_author()

        elif current_index == QueryIndex.LIST_ALL_PUBLISHERS.value:
            self.execute_list_all_publishers()

        elif current_index == QueryIndex.LIST_ALL_MEMBERS.value:
            self.execute_list_all_members()

        elif current_index == QueryIndex.LIST_MEMBERS_BY_BOOK.value:

            self.execute_list_all_member_by_book()
        elif current_index == QueryIndex.LIST_MEMBERS_BORROWED_AT_LEAST_ONE_BOOK.value:
            self.execute_list_members_borrowed_at_least_one_book()

    def execute_find_books_by_author(self) -> None:
        author_name = self.author_input.text().strip()
        if not author_name:
            QMessageBox.warning(self, "Warning", "Author name is not provided.")
            return
        try:
            ### YOUR CODE ###
            books = self.controller.get_book_by_author(author_name)
            ### YOUR CODE ###

        except Exception as e:
            logger.debug(str(e))
            QMessageBox.critical(self, "Error", "Failed to retrieve data. Check logs for debugging.")
            return

        self.populate_table(
            books,
            headers = ["Book ID", "Title", "Author", "Publisher ID", "ISBN", "Year"],
            data_formatter = lambda book: [
                str(book.id), book.title, book.author,
                str(book.publisher_id), book.isbn, str(book.year_published)
            ]
        )

    def execute_list_all_publishers(self) -> None:
        try:
            ### YOUR CODE ###
            publishers = self.controller.get_all_publishers()
            ### YOUR CODE ###
        except Exception as e:
            logger.debug(str(e))
            QMessageBox.critical(self, "Error", "Failed to retrieve data. Check logs for debugging.")
            return

        self.populate_table(
            publishers,
            headers = ["Publisher ID", "Name", "Address", "Phone", "Email"],
            data_formatter = lambda pub: [
                str(pub.id), pub.name, pub.address, pub.phone, pub.email
            ]
        )

    def execute_list_all_members(self) -> None:
        try:
            ### YOUR CODE ###
            members = self.controller.get_all_members()
            ### YOUR CODE ###
        except Exception as e:
            logger.debug(str(e))
            QMessageBox.critical(self, "Error", "Failed to retrieve data. Check logs for debugging.")
            return
        self.populate_table(
            members,
            headers = ["Member ID", "First Name", "Last Name", "Email", "Phone Number", "Address", "Membership Date"],
            data_formatter = lambda mem: [
                str(mem.id), mem.first_name, mem.last_name, mem.email, mem.phone, mem.address,
                str(mem.date_of_membership)
            ]
        )

    def execute_list_all_member_by_book(self):

        book_name = self.book_input.text().strip()
        if not book_name:
            QMessageBox.warning(self, "Warning", "Book title is not provided.")
            return
        try:
            ### YOUR CODE ###
            results = self.controller.get_all_member_by_book(book_name)
            ### YOUR CODE ###
        except Exception as e:
            logger.debug(str(e))
            QMessageBox.critical(self, "Error", "Failed to retrieve data. Check logs for debugging.")
            return
        self.populate_table(
            results,
            headers = ['First Name', 'Last Name', 'Title', "Date Borrowed", "Due Date", "Date Returned"],
            data_formatter = lambda r: [r[0], r[1], r[2], str(r[3]), str(r[4]), str(r[5])]
        )

    def execute_list_members_borrowed_at_least_one_book(self):

        try:
            ### YOUR CODE ###
            results = self.controller.get_all_loans()
            ### YOUR CODE ###
        except Exception as e:
            logger.debug(str(e))
            QMessageBox.warning(self, "Error", "Failed to retrieve data. Check logs for debugging.")
            return

        self.populate_table(
            results,
            headers = ['First Name', 'Last Name', 'Title', "Date Borrowed", "Due Date", "Date Returned"],
            data_formatter = lambda r: [r[0], r[1], r[2], str(r[3]), str(r[4]), str(r[5])]
        )

    def populate_table(self, items: List[object], headers: List[str], data_formatter: callable) -> None:
        """Helper method to populate the result table."""
        self.result_table.setRowCount(0)
        self.result_table.setColumnCount(len(headers))
        self.result_table.setHorizontalHeaderLabels(headers)

        for row_index, item in enumerate(items):
            self.result_table.insertRow(row_index)
            for col_index, data in enumerate(data_formatter(item)):
                self.result_table.setItem(row_index, col_index, QTableWidgetItem(data))
