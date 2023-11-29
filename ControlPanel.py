from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QTabWidget

from RadiatorControl import RadiatorControl


class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.living_room = RadiatorControl("Wohnzimmer")
        self.bed_room = RadiatorControl("Schlafzimmer")
        self.dining_room = RadiatorControl("Esszimmer")
        self.bath_room = RadiatorControl("Badezimmer")

        layout = QGridLayout(self)
        self.setLayout(layout)

        layout.addWidget(self.living_room, 1, 1)
        layout.addWidget(self.bed_room, 1, 2)
        layout.addWidget(self.dining_room, 1, 3)
        layout.addWidget(self.bath_room, 1, 4)

