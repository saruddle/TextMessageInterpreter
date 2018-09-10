# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextMessageGuiWidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MyWidget(object):
    def setupUi(self, textMessageInterpreterGuiWidget):
        textMessageInterpreterGuiWidget.setObjectName("textMessageInterpreterGuiWidget")
        textMessageInterpreterGuiWidget.resize(325, 271)
        self.verticalLayout = QtWidgets.QVBoxLayout(textMessageInterpreterGuiWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputMessageLabel = QtWidgets.QLabel(textMessageInterpreterGuiWidget)
        self.inputMessageLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputMessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputMessageLabel.setWordWrap(True)
        self.inputMessageLabel.setObjectName("inputMessageLabel")
        self.verticalLayout_2.addWidget(self.inputMessageLabel)
        self.textMessageInput = QtWidgets.QLineEdit(textMessageInterpreterGuiWidget)
        self.textMessageInput.setObjectName("textMessageInput")
        self.verticalLayout_2.addWidget(self.textMessageInput)
        self.translateButton = QtWidgets.QPushButton(textMessageInterpreterGuiWidget)
        self.translateButton.setFlat(False)
        self.translateButton.setObjectName("translateButton")
        self.verticalLayout_2.addWidget(self.translateButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.messageOutputLabel = QtWidgets.QLabel(textMessageInterpreterGuiWidget)
        self.messageOutputLabel.setEnabled(True)
        self.messageOutputLabel.setText("")
        self.messageOutputLabel.setTextFormat(QtCore.Qt.RichText)
        self.messageOutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageOutputLabel.setWordWrap(True)
        self.messageOutputLabel.setObjectName("messageOutputLabel")
        self.verticalLayout_2.addWidget(self.messageOutputLabel)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(textMessageInterpreterGuiWidget)
        # self.translateButton.clicked.connect(self.textMessageInput.copy)
        # self.translateButton.clicked.connect(self.messageOutputLabel.clear)
        QtCore.QMetaObject.connectSlotsByName(textMessageInterpreterGuiWidget)

    def retranslateUi(self, textMessageInterpreterGuiWidget):
        _translate = QtCore.QCoreApplication.translate
        textMessageInterpreterGuiWidget.setWindowTitle(_translate("textMessageInterpreterGuiWidget", "TMInterpreter"))
        self.inputMessageLabel.setText(_translate("textMessageInterpreterGuiWidget", "Please type in the text of the message you would like to have translated:"))
        self.translateButton.setText(_translate("textMessageInterpreterGuiWidget", "Translate"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    textMessageInterpreterGuiWidget = QtWidgets.QWidget()
#    ui = MyWidget()
#    ui.setupUi(textMessageInterpreterGuiWidget)
#    textMessageInterpreterGuiWidget.show()
#    sys.exit(app.exec_())


