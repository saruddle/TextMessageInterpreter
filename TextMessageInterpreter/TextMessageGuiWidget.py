# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextMessageGuiWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_textMessageInterpreterGuiWidget(object):
    def setupUi(self, textMessageInterpreterGuiWidget):
        textMessageInterpreterGuiWidget.setObjectName("textMessageInterpreterGuiWidget")
        textMessageInterpreterGuiWidget.resize(499, 407)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        textMessageInterpreterGuiWidget.setFont(font)
        textMessageInterpreterGuiWidget.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(textMessageInterpreterGuiWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputMessageLabel = QtWidgets.QLabel(textMessageInterpreterGuiWidget)
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.inputMessageLabel.setFont(font)
        self.inputMessageLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputMessageLabel.setWordWrap(True)
        self.inputMessageLabel.setObjectName("inputMessageLabel")
        self.verticalLayout_2.addWidget(self.inputMessageLabel)
        self.textMessageInput = QtWidgets.QLineEdit(textMessageInterpreterGuiWidget)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.textMessageInput.setFont(font)
        self.textMessageInput.setObjectName("textMessageInput")
        self.verticalLayout_2.addWidget(self.textMessageInput)
        self.translateButton = QtWidgets.QPushButton(textMessageInterpreterGuiWidget)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.translateButton.setFont(font)
        self.translateButton.setStyleSheet("QPushButton#translateButton {padding: 15px 25px; text-align: center; outline: none; color: #fff; background-color: #4CAF50; border: none; border-radius: 15px}\n"
"QPushButton#translateButton:hover {background-color:  rgb(0, 0, 255); border: none}")
        self.translateButton.setFlat(False)
        self.translateButton.setObjectName("translateButton")
        self.verticalLayout_2.addWidget(self.translateButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.outputHeader = QtWidgets.QLabel(textMessageInterpreterGuiWidget)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.outputHeader.setFont(font)
        self.outputHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputHeader.setLineWidth(3)
        self.outputHeader.setText("")
        self.outputHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.outputHeader.setObjectName("outputHeader")
        self.verticalLayout_2.addWidget(self.outputHeader)
        self.messageOutputLabel = QtWidgets.QLabel(textMessageInterpreterGuiWidget)
        self.messageOutputLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.messageOutputLabel.setFont(font)
        self.messageOutputLabel.setText("")
        self.messageOutputLabel.setTextFormat(QtCore.Qt.RichText)
        self.messageOutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageOutputLabel.setWordWrap(True)
        self.messageOutputLabel.setObjectName("messageOutputLabel")
        self.verticalLayout_2.addWidget(self.messageOutputLabel)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(textMessageInterpreterGuiWidget)
        QtCore.QMetaObject.connectSlotsByName(textMessageInterpreterGuiWidget)

    def retranslateUi(self, textMessageInterpreterGuiWidget):
        _translate = QtCore.QCoreApplication.translate
        textMessageInterpreterGuiWidget.setWindowTitle(_translate("textMessageInterpreterGuiWidget", "Text Message Translater"))
        self.inputMessageLabel.setText(_translate("textMessageInterpreterGuiWidget", "Please type in the text of the message you would like to have translated:"))
        self.translateButton.setText(_translate("textMessageInterpreterGuiWidget", "Translate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    textMessageInterpreterGuiWidget = QtWidgets.QWidget()
    ui = Ui_textMessageInterpreterGuiWidget()
    ui.setupUi(textMessageInterpreterGuiWidget)
    textMessageInterpreterGuiWidget.show()
    sys.exit(app.exec_())

