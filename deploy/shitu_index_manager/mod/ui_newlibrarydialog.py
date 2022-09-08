# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/NewlibraryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewlibraryDialog(object):
    def setupUi(self, NewlibraryDialog):
        NewlibraryDialog.setObjectName("NewlibraryDialog")
        NewlibraryDialog.resize(414, 230)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewlibraryDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(NewlibraryDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.indexMethodCmb = QtWidgets.QComboBox(NewlibraryDialog)
        self.indexMethodCmb.setEnabled(True)
        self.indexMethodCmb.setObjectName("indexMethodCmb")
        self.indexMethodCmb.addItem("")
        self.indexMethodCmb.addItem("")
        self.indexMethodCmb.addItem("")
        self.verticalLayout.addWidget(self.indexMethodCmb)
        self.resetCheckBox = QtWidgets.QCheckBox(NewlibraryDialog)
        self.resetCheckBox.setObjectName("resetCheckBox")
        self.verticalLayout.addWidget(self.resetCheckBox)
        spacerItem = QtWidgets.QSpacerItem(20, 80,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewlibraryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel
                                          | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewlibraryDialog)
        self.indexMethodCmb.setCurrentIndex(0)
        self.buttonBox.accepted.connect(NewlibraryDialog.accept)
        self.buttonBox.rejected.connect(NewlibraryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewlibraryDialog)

    def retranslateUi(self, NewlibraryDialog):
        _translate = QtCore.QCoreApplication.translate
        NewlibraryDialog.setWindowTitle(
            _translate("NewlibraryDialog", "新建/重建 索引"))
        self.label.setText(_translate("NewlibraryDialog", "索引方式"))
        self.indexMethodCmb.setItemText(
            0, _translate("NewlibraryDialog", "HNSW32"))
        self.indexMethodCmb.setItemText(1,
                                        _translate("NewlibraryDialog", "FLAT"))
        self.indexMethodCmb.setItemText(2, _translate("NewlibraryDialog",
                                                      "IVF"))
        self.resetCheckBox.setText(
            _translate("NewlibraryDialog", "重建索引，警告：会覆盖原索引"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewlibraryDialog = QtWidgets.QDialog()
    ui = Ui_NewlibraryDialog()
    ui.setupUi(NewlibraryDialog)
    NewlibraryDialog.show()
    sys.exit(app.exec_())