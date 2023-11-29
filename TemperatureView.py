from PyQt6 import QtCharts
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QHeaderView, QHBoxLayout, QSizePolicy, QTableView, QVBoxLayout
from PyQt6.QtGui import QPainter
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis, QDateTimeAxis


class TemperatureView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        chart = QtCharts.QChart()
        chart.setTitle("Temperaturverlauf")

        # Zeitachse
        #time_axis = QtCharts.QDateTimeAxis()
        #time_axis.setFormat("hh:mm")
        #chart.addAxis(time_axis, Qt.AlignmentFlag.AlignBottom)

        # Temperaturachse
        #temp_axis = QtCharts.QValueAxis()
        #temp_axis.setTitleText("Temperatur (°C)")
        #chart.addAxis(temp_axis, Qt.AlignmentFlag.AlignLeft)

        # Datenpunkte
        #series = QtCharts.QLineSeries()
        #series.append(QDateTime.currentDateTime().addSecs(0), 20)
        #series.append(QDateTime.currentDateTime().addSecs(3600), 21)
        #series.append(QDateTime.currentDateTime().addSecs(7200), 22)

        #chart.addSeries(series)

        # ChartView
        #chart_view = QtCharts.QChartView(chart)
        #chart_view.setRenderHint(QtCharts.QChartView.RenderHint.Antialiasing)

        # ChartView
        #chart_view = QChartView(chart)
        #chart_view.setRenderHint(QChartView.RenderHint.Antialiasing)

        #self.setCentralWidget(chart_view)
        #self.setWindowTitle("Temperaturdiagramm")


