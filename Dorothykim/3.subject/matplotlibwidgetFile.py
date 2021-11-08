# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(6)
# years = ['2015', '2016', '2017', '2018', '2019','2020']
# values = [100, 400, 900, 200, 300, 500]
#
# plt.bar(x, values)
# plt.xticks(x, years)
#
# plt.show()
#

# from PyQt5.QtWidgets import*
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
#
# class matplotlibWidget(QWidget):
#
#     def __init__(self, parent = None):
#         QWidget.__init__(self, parent)
#         self.canvas = FigureCanvas(Figure())
#         vertical_layout=QVBoxLayout()
#         vertical_layout.addWidget(self.canvas)
#         vertical_layout.setContentsMargins(1, 1, 1, 1)
#         self.canvas.axes=self.canvas.figure.add_subplot(111)
#         self.setLayout(vertical_layout)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MyApp(QMainWindow):

  def __init__(self):
      super().__init__()

      self.main_widget = QWidget()
      self.setCentralWidget(self.main_widget)

      canvas = FigureCanvas()
      vbox = QVBoxLayout(self.main_widget)
      vbox.addWidget(canvas)

      self.addToolBar(NavigationToolbar(canvas, self))

      self.ax = canvas.figure.subplots()
      self.ax.plot([0, 1, 2], [1, 5, 3], '-')

      self.setWindowTitle('Matplotlib in PyQt5')
      self.setGeometry(300, 100, 600, 400)
      self.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())