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

from PySide2.QtGui import QPixmap, Qt
from PySide2.QtWidgets import QFrame, QLabel, QVBoxLayout


class GCLogoView(QFrame):
    """Logo View

        Summary:
            A class for GCLogoView that includes:

            -Pixmap in a label in center of frame

        Attributes:
            logo, main_layout, pixmap

        Methods:
            None

        Attributes
        ----------
            main_layout : QVBoxLayout
            logo : QLabel
                Label for storing logo pixmap
            pixmap : QPixmap
                Pixmap for logo display

        Methods
        -------
            None
    """
    def __init__(self, parent=None):
        """Constructor:
            Initialize Logo View

            Parameters:
                self
                parent : QFrame
            Returns:
                None
        """
        super(GCLogoView, self).__init__(parent)

        self.logo = QLabel(self)
        pixmap = QPixmap('../GC_Images/logo.png')
        self.logo.setPixmap(pixmap)

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.logo, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)
