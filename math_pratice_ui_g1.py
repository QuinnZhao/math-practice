# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'math_g1_test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from constants import TYPES

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(796, 652)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 751, 611))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cbbType = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.cbbType.setFont(font)
        self.cbbType.setObjectName("cbbType")
        '''
        self.types = ["20以内加",
                      "和为20到100两位数加",
                      "100以内两位数减",
                      "100以内加减运算",
                      "10以内连加",
                      "10以内连减",
                      "10以内混合加减"]
        '''
        self.types = TYPES
        for item in self.types:
            self.cbbType.addItem("")
        self.horizontalLayout_2.addWidget(self.cbbType)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cbbNum = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.cbbNum.setFont(font)
        self.cbbNum.setObjectName("cbbNum")
        self.cbbNum.addItem("")
        self.cbbNum.addItem("")
        self.horizontalLayout_2.addWidget(self.cbbNum)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnGen = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnGen.setFont(font)
        self.btnGen.setObjectName("btnGen")
        self.horizontalLayout.addWidget(self.btnGen)
        self.btnExport = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnExport.setFont(font)
        self.btnExport.setObjectName("btnExport")
        self.horizontalLayout.addWidget(self.btnExport)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.teItems = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.teItems.setFont(font)
        self.teItems.setReadOnly(True)
        self.teItems.setTabStopWidth(80)
        self.teItems.setObjectName("teItems")
        self.verticalLayout.addWidget(self.teItems)

        self.retranslateUi(Form)
        self.btnGen.clicked.connect(Form.generate)

        self.btnExport.clicked.connect(Form.export)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "一年级数学加减口算出题系统"))
        self.label.setText(_translate("Form", "题型"))
        for index, value in enumerate(self.types):
            self.cbbType.setItemText(index, _translate("Form" , value))
            
        self.label_2.setText(_translate("Form", "题目数"))
        
        self.cbbNum.setItemText(0, _translate("Form", "50"))
        self.cbbNum.setItemText(1, _translate("Form", "100"))
        
        self.btnGen.setText(_translate("Form", "出题"))
        self.btnExport.setText(_translate("Form", "导出"))
        self.teItems.setDocumentTitle(_translate("Form", "一年级10以内加减混合口算练习题"))
        
