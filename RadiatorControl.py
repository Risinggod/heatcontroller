from PyQt6.QtWidgets import QWidget, QLCDNumber, QDial, QLabel, QGridLayout


class RadiatorControl(QWidget):
    def __init__(self, raumname, parent=None):
        super().__init__(parent)

        self.label1 = QLabel(raumname)

        self.sollT = QLCDNumber()
        self.istT = QLCDNumber()

        self.regler = QDial()
        self.regler.setRange(15, 30)

        self.regler.valueChanged.connect(self.sollT.display)

        layout = QGridLayout(self)
        self.setLayout(layout)

        layout.addWidget(self.label1, 1, 1)
        layout.addWidget(self.sollT, 2, 1)
        layout.addWidget(self.istT, 3, 1)
        layout.addWidget(self.regler, 4, 1)