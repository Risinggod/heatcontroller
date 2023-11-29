from PyQt6.QtWidgets import QMainWindow, QTabWidget, QLabel, QGridLayout
from ControlPanel import ControlPanel
from TemperatureView import TemperatureView
from  Heater import Heater
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        tabwidget = QTabWidget()

        layout1 = QGridLayout(self)
        self.setLayout(layout1)


        controlpanel = ControlPanel(parent)

        heater = Heater(parent)

        temperatureView = TemperatureView(parent)

        self.setCentralWidget(tabwidget)

        self.setWindowTitle("Heizungssteuerung")

        tabwidget.addTab(controlpanel, "steuerung")
        tabwidget.addTab(heater, "Heizungsanlage")
        tabwidget.addTab(temperatureView, "Temperaturverlauf")



