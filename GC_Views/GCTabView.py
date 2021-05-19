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

from PySide2 import QtCore
from PySide2.QtWidgets import QTabWidget, QFrame, QVBoxLayout, QApplication, QHBoxLayout, QPushButton, QMessageBox, \
    QLabel
from GC_Views.GCHomeView import GCHomeView
from GC_Views.GCResultsOutputView import GCResultsOutputView
from GC_Views.GCTableView import GCTableView
from GC_Services.FileIo import FileIo


class GCTabView(QFrame):
    """GC Tab View

        Summary:
            A class for {Type} that includes:

            -{Description} to the {Location eg left}

        Attributes:


        Methods:


        Attributes
        ----------


        Methods
        -------

    """
    def __init__(self, parent=None, file_io=FileIo()):
        # -------------------------------------------init Start-------------------------------------------
        super(GCTabView, self).__init__(parent)
        self.fio = file_io

        # Views for tabs
        self.hv_homeView = GCHomeView(None,self.fio)
        self.tv_tableView = GCTableView(None,self.fio)
        self.rv_resultsView = GCResultsOutputView(None,self.fio)

        # ----------------------------------------------
        # -----------------hbl_tab_layout-----------------
        # ----------------------------------------------
        self.hbl_tab_layout = QHBoxLayout()

        self.tw_tabWidget = QTabWidget()
        self.tw_tabWidget.setStyleSheet("QTabBar::tab {font:Verdana;height:55%;border:3px solid #1000A0;width:390%;"
                                        "background-color:white;color:#1000A0; border-bottom:2px dashed #1000A0;"
                                        "font-weight:600;font-size:14px;margin:0 auto -17 auto;border-radius:13px;}"
                                        "QTabBar::tab:selected{background-color:#1000A0;color:white;}")

        self.tw_tabWidget.insertTab(0, self.hv_homeView, "Project Setup - Configure Directory for Project Mapping")
        self.tw_tabWidget.insertTab(1, self.tv_tableView, "Asset Selection - Load CSV and Select Assets")
        self.tw_tabWidget.insertTab(2, self.rv_resultsView, "Review and Check")

        self.tw_tabWidget.setTabEnabled(0, True)
        self.tw_tabWidget.setTabEnabled(1, False)
        self.tw_tabWidget.setTabEnabled(2, False)

        self.hbl_tab_layout.addWidget(self.tw_tabWidget)
        # -------------------------------------------------
        # -----------------hbl_nav_buttons_layout-----------------
        # -------------------------------------------------

        self.hbl_nav_buttons_layout = QHBoxLayout()

        self.spacer = QLabel("")
        self.btn_back = QPushButton(text="Back")
        self.btn_continue = QPushButton(text="Continue")
        self.btn_back.setStyleSheet("margin:3 auto;color:#1000A0; background-color:rgb(255,255,255);padding:10;"
                                    "border:2px solid #1000A0;border-radius:20px;font-weight:600;")

        self.btn_back.clicked.connect(self.back_clicked)
        self.btn_continue.clicked.connect(self.continue_clicked)

        self.hbl_nav_buttons_layout.addWidget(self.spacer)
        self.hbl_nav_buttons_layout.addWidget(self.spacer)
        self.hbl_nav_buttons_layout.addWidget(self.btn_back)
        self.hbl_nav_buttons_layout.addWidget(self.btn_continue)

        # -------------------------------------------------
        # -----------------vbl_main_layout-----------------
        # -------------------------------------------------

        self.vbl_main_layout = QVBoxLayout()

        self.vbl_main_layout.addLayout(self.hbl_tab_layout)
        self.vbl_main_layout.addLayout(self.hbl_nav_buttons_layout)

        self.setLayout(self.vbl_main_layout)
        self.setStyleSheet('GCTableView{border:4px solid #1000A0;margin:0;padding:0} '
                           'GCHomeView{border:4px solid #1000A0;margin:0;} '
                           'GCResultsOutputView{border:4px solid #1000A0;margin:0}')

        # -------------------------------------------init End-------------------------------------------

    def set_tab_index(self, index_num=0):
        current_index = self.get_tab_index()
        self.tw_tabWidget.setTabEnabled(current_index, False)

        self.tw_tabWidget.setCurrentIndex(index_num)
        self.tw_tabWidget.setTabEnabled(index_num, True)

    def get_tab_index(self):
        return self.tw_tabWidget.currentIndex()

    def continue_clicked(self):
        tab_index = self.get_tab_index()
        if tab_index == 0:
            self.home_view_transition()
        elif tab_index == 1:
            self.table_view_transition()
        elif tab_index == 2:
            pass

    def dirs_are_valid(self):
        project_path = self.hv_homeView.cdv_create_view.ldi_main_path.get_input_text()
        animatic_path = self.hv_homeView.cdv_create_view.ldi_animatics_path.get_input_text()
        asset_path = self.hv_homeView.cdv_create_view.ldi_asset_path.get_input_text()
        episode_path = self.hv_homeView.cdv_create_view.ldi_episode_path.get_input_text()
        sound_path = self.hv_homeView.cdv_create_view.ldi_sounds_path.get_input_text()

        valid_project_path = self.fio.validate_path(project_path)
        valid_animatic_path = self.fio.validate_path(animatic_path)
        valid_asset_path = self.fio.validate_path(asset_path)
        valid_episode_path = self.fio.validate_path(episode_path)
        valid_sound_path = self.fio.validate_path(sound_path)

        if valid_project_path and valid_animatic_path and valid_asset_path and valid_episode_path and valid_sound_path:
            return True
        else:
            warning_message = "Errors detected in path mapping!"
            warning_message += "\nPlease ensure the following directories exist!"
            if not valid_project_path:
                warning_message += f"\nInvalid - Project Path: {project_path}"
            if not valid_asset_path:
                warning_message += f"\nInvalid - Asset Path: {asset_path}"
            if not valid_animatic_path:
                warning_message += f"\nInvalid - Animatic Path: {animatic_path}"
            if not valid_episode_path:
                warning_message += f"\nInvalid - Episode Path: {episode_path}"
            if not valid_sound_path:
                warning_message += f"\nInvalid - Sound Path: {sound_path}"

            self.issue_warning_prompt(warning_message)
            return False

    def home_view_transition(self):
        frame_index = self.hv_homeView.get_frame_index()
        if frame_index == 0:
            self.issue_warning_prompt("Please setup default directory structure!")

        elif frame_index == 1:
            if self.dirs_are_valid():
                self.hv_homeView.cdv_create_view.update_fio()
                self.tv_tableView.lfi_file_select.set_input_text(self.fio.project_dir)
                self.set_tab_index(1)

    def table_view_transition(self):
        selection = self.tv_tableView.create_selection()
        if selection:
            self.rv_resultsView.load_table_data(selection)
            self.set_tab_index(2)
        else:
            self.issue_warning_prompt("No shots were selected. Cannot Proceed!")

    def issue_warning_prompt(self, message=""):
        msg_warning = QMessageBox()
        msg_warning.setIcon(QMessageBox.Warning)
        msg_warning.setText(message)
        msg_warning.exec_()

    def back_clicked(self):
        tab_index = self.get_tab_index()
        if tab_index == 0:
            pass
        elif tab_index == 1:
            self.set_tab_index(0)
        elif tab_index == 2:
            self.set_tab_index(1)



if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tabview = GCTabView()
    tabview.show()
    # directory.show()
    sys.exit(qApp.exec_())
