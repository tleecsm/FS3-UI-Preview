# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:12:02 2018

@author: Tanner Lee
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi

class SimpleCounter(QMainWindow):
    def __init__(self):
        super(SimpleCounter,self).__init__()
        loadUi('fs3.ui',self)
        self.mainWindowSplitter.setStretchFactor(1,10)
        self.counter = 0
        self.setWindowTitle('FS3 -- FieldStats3')


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)      
if not QApplication.instance():
    app=QApplication(sys.argv)
else: 
    app=QApplication.instance()
widget=SimpleCounter()
widget.show()
sys.exit(app.exec_())
