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


from PySide2.QtWidgets import QFrame, QVBoxLayout

from GC_Components.InputComponents import LabeledDirectoryInput


class ServerSelectionView(QFrame):
    """Server Selection View

                    Summary:
                        A class for {Type} that includes:

                        -{Description} to the {Location eg left}

                    Attributes:
                        label, {AttributeName}

                    Methods:
                        get_input_text, {MethodName}

                    Attributes
                    ----------
                        label : QLabel
                            Text Label for Input Box
                        {AttributeName} : {AttributeClass}
                            {Property} for {Type}

                    Methods
                    -------
                        get_input_text(self)
                            Return the text in the input box
                        {MethodName}({Parameters})
                            {Functionality}
                """
    def __init__(self, parent=None):
        super(ServerSelectionView, self).__init__(parent)

        self.serverPath = LabeledDirectoryInput(self, label_text="Select Server Directory: ")
        self.localPath = LabeledDirectoryInput(self, label_text="Select Local Directory: ")

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.serverPath)
        self.main_layout.addWidget(self.localPath)
        self.setLayout(self.main_layout)
        self.setStyleSheet('border:none')
        self.topLevelWidget().setStyleSheet('QFrame{border:none} '
                                            'LabeledDirectoryInput::QLineEdit{border:1px solid #1000A0}')

