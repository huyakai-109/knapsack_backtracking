from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Palette
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 99, 71))
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255, 99, 71))
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 99, 71))
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(0, 0, 0))
        self.centralwidget.setPalette(palette)

        # Font
        font = QtGui.QFont()
        font.setPointSize(14)

        # Labels
        self.values_label = QtWidgets.QLabel(self.centralwidget)
        self.values_label.setGeometry(QtCore.QRect(10, 10, 151, 50))
        self.values_label.setObjectName("values_label")
        self.values_label.setStyleSheet(
            "border: 1px solid #ccc; border-radius: 5px; padding: 5px;")

        self.weights_label = QtWidgets.QLabel(self.centralwidget)
        self.weights_label.setGeometry(QtCore.QRect(10, 70, 151, 50))
        self.weights_label.setObjectName("weights_label")
        self.weights_label.setStyleSheet(
            "border: 1px solid #ccc; border-radius: 5px; padding: 5px;")

        self.max_weight_label = QtWidgets.QLabel(self.centralwidget)
        self.max_weight_label.setGeometry(QtCore.QRect(10, 130, 151, 50))
        self.max_weight_label.setObjectName("max_weight_label")
        self.max_weight_label.setStyleSheet(
            "border: 1px solid #ccc; border-radius: 5px; padding: 5px;")

        # LineEdits
        self.values_input = QtWidgets.QLineEdit(self.centralwidget)
        self.values_input.setGeometry(QtCore.QRect(170, 10, 311, 51))
        self.values_input.setObjectName("values_input")
        self.values_input.setFont(font)

        self.weights_input = QtWidgets.QLineEdit(self.centralwidget)
        self.weights_input.setGeometry(QtCore.QRect(170, 70, 311, 51))
        self.weights_input.setObjectName("weights_input")
        self.weights_input.setFont(font)

        self.max_weight_input = QtWidgets.QLineEdit(self.centralwidget)
        self.max_weight_input.setGeometry(QtCore.QRect(170, 130, 311, 51))
        self.max_weight_input.setObjectName("max_weight_input")
        self.max_weight_input.setFont(font)

        # Buttons
        self.solve_button = QtWidgets.QPushButton(self.centralwidget)
        self.solve_button.setGeometry(QtCore.QRect(170, 190, 150, 41))
        self.solve_button.setObjectName("solve_button")

        self.random_button = QtWidgets.QPushButton(self.centralwidget)
        self.random_button.setGeometry(QtCore.QRect(10, 190, 150, 41))
        self.random_button.setObjectName("random_button")

        self.show_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_button.setGeometry(QtCore.QRect(330, 190, 150, 41))
        self.show_button.setObjectName("show_button")

        # Result TextBrowser
        self.result_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(10, 240, 471, 151))
        self.result_label.setObjectName("result_label")
        self.result_label.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        # MenuBar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # StatusBar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Translate UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Knapsack Problem Solver"))
        self.values_label.setText(_translate("MainWindow", "Giá trị:"))
        self.weights_label.setText(_translate("MainWindow", "Khối lượng:"))
        self.max_weight_label.setText(
            _translate("MainWindow", "Khối lượng túi:"))
        self.solve_button.setText(_translate("MainWindow", "Solve"))
        self.random_button.setText(_translate("MainWindow", "Random"))
        self.show_button.setText(_translate("MainWindow", "Biểu đồ"))
