from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel




class Heater(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout(self)

        self.testLabel = QLabel("das ist ein test")
        layout.addWidget(self.testLabel, 1, 1)

        self.setLayout(layout)


