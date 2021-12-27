from PyQt5.QtCore import QThread, pyqtSignal
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QGridLayout
from communicationThread import *
from mainWindowUI import *
import time

class MplCanvas(FigureCanvas):
    def __init__(self, width = 5, height = 4, dpi = 100):
        figure = Figure(figsize = (width, height), dpi = dpi,  tight_layout = 3.0)
        self.axes = figure.add_subplot(211)
        self.axes1 = figure.add_subplot(212)
        self.axes.set_title('Humidity')
        self.axes1.set_title('Temperature')
        self.axes.set_xlabel('Samples')
        self.axes1.set_xlabel('Samples')
        self.axes.set_ylabel('%', fontsize = 16)
        self.axes1.set_ylabel('°C', fontsize = 16)

        super().__init__(figure)


class MyGraphThread(QThread):
    def __init__(self, tabPlot):
        super().__init__()
        self.canvas = MplCanvas()
        self.mpl = QGridLayout() #Pravimo gridLayout
        self.mpl.addWidget(self.canvas)
        tabPlot.setLayout(self.mpl) #Na tabPlot primeni gore napravljeni tab
        self.ydata = [None]*10 #Lista od 10 elemenata None
        self.ydata1 = [None]*10
        self.xdata = list(range(10))#Funkija range nam vraca 10 elemenata u ovom slicaju brojeve od 1 do 10 redom
        self.xdata1 = list(range(10))

    def run(self):
         while(1):
            time.sleep(10)
    def up_graph(self, data):
        try:
            self.ydata = self.ydata[1:]
            self.ydata1 = self.ydata1[1:]
            self.ydata.append(float(data[0]))#Osvezavamo listu kako se pojavi novi element
            self.ydata1.append(float(data[1]))
            print(self.ydata)
            print(self.ydata1)
            print(self.xdata)
        except:
            self.ydata.append(None)
            self.ydata1.append(None)
            print('Problem u konverziji')

        #Humidity
        
        self.canvas.axes.cla() #cla funkija koja brise sve podatke sa grafika
        self.canvas.axes.plot(self.xdata, self.ydata, 'r') #sta hocemo da iscrtamo
        #Temperature
        
        self.canvas.axes1.cla() #cla funkija koja brise sve podatke sa grafika
        self.canvas.axes1.plot(self.xdata1, self.ydata1, 'g') #sta hocemo da iscrtamo
        
        self.canvas.axes.set_title('Humidity')
        self.canvas.axes.set_ylabel('%', fontsize = 16)
        self.canvas.axes1.set_title('Temperature')
        self.canvas.axes1.set_ylabel('°C', fontsize = 16)

        self.canvas.draw()#funkija za crtanje
    
    def exit(self):
        self.terminate()