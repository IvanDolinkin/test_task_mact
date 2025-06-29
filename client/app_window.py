# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QSplitter, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(545, 352)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(84, 176, 248, 255), stop:1 rgba(34, 96, 145, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter_4 = QSplitter(self.centralwidget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(20, 20, 191, 220))
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.AddButton = QPushButton(self.splitter_4)
        self.AddButton.setObjectName(u"AddButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        self.AddButton.setMaximumSize(QSize(16777215, 40))
        self.AddButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 5px;")
        self.splitter_4.addWidget(self.AddButton)
        self.GetButton = QPushButton(self.splitter_4)
        self.GetButton.setObjectName(u"GetButton")
        sizePolicy.setHeightForWidth(self.GetButton.sizePolicy().hasHeightForWidth())
        self.GetButton.setSizePolicy(sizePolicy)
        self.GetButton.setMaximumSize(QSize(16777215, 40))
        self.GetButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 5px;")
        self.splitter_4.addWidget(self.GetButton)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.splitter_3)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 5px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_3.addWidget(self.label)
        self.comboBox = QComboBox(self.splitter_3)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));")
        self.splitter_3.addWidget(self.comboBox)
        self.splitter_4.addWidget(self.splitter_3)
        self.splitter = QSplitter(self.splitter_4)
        self.splitter.setObjectName(u"splitter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.labelPage = QLabel(self.splitter)
        self.labelPage.setObjectName(u"labelPage")
        self.labelPage.setMaximumSize(QSize(16777215, 40))
        self.labelPage.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 5px;")
        self.labelPage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.labelPage)
        self.spinBox = QSpinBox(self.splitter)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy3)
        self.spinBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));")
        self.splitter.addWidget(self.spinBox)
        self.labelOf = QLabel(self.splitter)
        self.labelOf.setObjectName(u"labelOf")
        self.labelOf.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 5px;")
        self.labelOf.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter.addWidget(self.labelOf)
        self.splitter_4.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_4)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy2.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy2)
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.PrevButton = QPushButton(self.splitter_2)
        self.PrevButton.setObjectName(u"PrevButton")
        sizePolicy2.setHeightForWidth(self.PrevButton.sizePolicy().hasHeightForWidth())
        self.PrevButton.setSizePolicy(sizePolicy2)
        self.PrevButton.setMaximumSize(QSize(16777215, 40))
        self.PrevButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 5px;")
        self.splitter_2.addWidget(self.PrevButton)
        self.NextButton = QPushButton(self.splitter_2)
        self.NextButton.setObjectName(u"NextButton")
        sizePolicy2.setHeightForWidth(self.NextButton.sizePolicy().hasHeightForWidth())
        self.NextButton.setSizePolicy(sizePolicy2)
        self.NextButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 5px;")
        self.splitter_2.addWidget(self.NextButton)
        self.splitter_4.addWidget(self.splitter_2)
        self.splitter_5 = QSplitter(self.centralwidget)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(240, 20, 281, 311))
        self.splitter_5.setMaximumSize(QSize(16777215, 16777215))
        self.splitter_5.setOrientation(Qt.Orientation.Vertical)
        self.lineEdit = QLineEdit(self.splitter_5)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 40))
        self.lineEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 10px;")
        self.splitter_5.addWidget(self.lineEdit)
        self.listView = QListView(self.splitter_5)
        self.listView.setObjectName(u"listView")
        sizePolicy2.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy2)
        self.listView.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.5 rgba(252, 207, 117, 255), stop:1 rgba(244, 143, 60, 255));\n"
"border-radius: 10px;")
        self.splitter_5.addWidget(self.listView)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ItemsApp", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"Add item", None))
        self.GetButton.setText(QCoreApplication.translate("MainWindow", u"Get items", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Items on page", None))
        self.labelPage.setText(QCoreApplication.translate("MainWindow", u"Page", None))
        self.labelOf.setText(QCoreApplication.translate("MainWindow", u"Of", None))
        self.PrevButton.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.NextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

