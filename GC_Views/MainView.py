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

from PySide2.QtGui import QGuiApplication
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QStatusBar, QVBoxLayout, QMessageBox
from TabView import TabView
from GC_Components.MainComponents import MenuBar, MainButtons
from DummyView import DummyView


class MainView(QMainWindow):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.tabFrame = QFrame()
        self.tab_widget = TabView()
        self.dummy = DummyView()
        self.tabIndex = self.tab_widget.tabIndex

        # self.results = []

        # Menu Bar
        self.menuBar = MenuBar(self)
        self.setMenuBar(self.menuBar)

        # Status Bar
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("This is a status message.", 5000)
        self.setStatusBar(self.statusBar)

        # Cancel and Continue Buttons
        self.btnBox = MainButtons(self)
        self.btnBox.continueBtn.clicked.connect(self.continue_clicked)
        self.btnBox.cancelBtn.clicked.connect(self.cancel_clicked)

        # Main window
        self.layout.addWidget(self.tab_widget)
        self.layout.addItem(self.btnBox)
        self.tabFrame.setLayout(self.layout)
        self.setCentralWidget(self.tabFrame)
        self.setWindowTitle("Glass Carbide")
        # self.setGeometry(0, 0, 900, 600)
        self.centralWidget().setMinimumSize(900, 600)
        self.setStyleSheet("background-color: white;")
        self.center_screen()

    def center_screen(self):
        screen = self.topLevelWidget().screen().geometry()
        self.resize(screen.width()/1.25, screen.height()/1.5)
        size = self.size()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 3)

    def continue_clicked(self):
        if self.tab_widget.homeView.mappingView.get_dir_path():
            self.tab_widget.dir_getter()

        tab_index = self.tab_widget.tabIndex

        if tab_index == 0:
            self.tab_widget.tab_index_setter(1)
        elif tab_index == 1:
            results = self.tab_widget.tableView.create_selection()
            self.tab_widget.tab_index_setter(2)
            self.tab_widget.resultsView.load_table_data(results)

            self.dummy.setStyleSheet('margin:0; padding:0')
            self.dummy.table.setStyleSheet('border:none; margin:0; padding:0')
            self.dummy.table.table.setStyleSheet('border:1px dotted grey; margin:0; padding:0')



        elif tab_index == 2:
            msg = QMessageBox()
            msg.setWindowTitle("Are you sure?")
            msg.setText("Open { Project Name } in { Software }?")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
        else:
            pass

    def cancel_clicked(self):
        tab_index = self.tab_widget.tabIndex

        if tab_index == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Save your progress?")
            msg.setText("Would you like to save your progress?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Close)
            msg.exec_()
        elif tab_index == 1:
            self.tab_widget.tab_index_setter(0)
        elif tab_index == 2:
            self.tab_widget.tab_index_setter(1)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = MainView()
    mainBase.show()
    # directory.show()
    sys.exit(qApp.exec_())
