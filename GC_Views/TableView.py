# Project Name:
# Glass Carbide
#
# By:
# Michael Gailling
# &&
# Mustafa Butt
#
# Organization:
# WIMTACH
#
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout, QTableWidgetItem

from GC_Components.InputComponents import LabeledFileInput
from GC_Components.TableComponents import DataTable
from GC_Services.csvIO import CsvIo


class TableView(QFrame):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.vBox = QVBoxLayout()
        self.csv_handler = CsvIo()

        # Table
        self.dt_table = DataTable(self)
        self.column_definitions = []

        # Labeled File Input
        self.lfi_file_select = LabeledFileInput(self, label_text="Select CSV", file_type="CSV Format (*.csv)")

        # Load Button
        self.btn_load_file = QPushButton("Load To Table")
        self.btn_load_file.setStyleSheet("background-color:blue;color:white;padding:10;border : 2px solid blue;"
                                         "border-radius:20px")
        self.btn_load_file.clicked.connect(self.load_file)

        # Layout loading
        self.vBox.addWidget(self.dt_table)
        self.vBox.addWidget(self.lfi_file_select)
        self.vBox.addWidget(self.btn_load_file, alignment=Qt.AlignHCenter)
        self.setLayout(self.vBox)
 
        self.setGeometry(0, 0, 800, 500)

    def load_file(self):
        self.csv_handler.data.clear()
        input_path = self.lfi_file_select.get_input_text()

        if input_path:
            self.csv_handler.import_data(input_path)

            csv_headers = self.csv_handler.data.pop(0)
            csv_headers.insert(0, "Select")
            csv_data = self.csv_handler.data

            self.dt_table.load_data(csv_data)

            self.dt_table.insert_control_row("combobox", 0, ["None", "File Name", "Asset Path"])

            self.dt_table.insert_control_column("checkbox", 1)

            self.dt_table.set_headers(csv_headers)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = TableView()
    tab.show()
    sys.exit(qApp.exec_())

