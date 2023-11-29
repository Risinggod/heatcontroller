from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel




class Heater(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.testLabel = QLabel("das ist ein test")

        layout = QGridLayout(self)
        self.setLayout(layout)

        layout.addWidget(self.testLabel, 1, 1)

