import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('Demo QSpinBox')
        self.fontLabel = QLabel('Jenis huruf')
        self.fontCombo = QFontComboBox()
        self.fontCombo.setEditable(False)
        self.sizeLabel = QLabel('Ukuran huruf')
        self.sizeSpinBox = QSpinBox()
        self.sizeSpinBox.setRange(8,20)
        self.sizeSpinBox.setSingleStep(1)
        self.sizeSpinBox.setValue(18)
        self.sampleLabel = QLabel('Contoh Teks')
        self.sampleLabel.setFont(QFont('DejaVu Sans',18))
        layout = QGridLayout()
        layout.addWidget(self.fontLabel, 0, 0)
        layout.addWidget(self.fontCombo, 0, 1)
        layout.addWidget(self.sizeLabel, 1, 0)
        layout.addWidget(self.sizeSpinBox, 1, 1)
        layout.addWidget(self.sampleLabel, 2, 0, 1, 2)
        #layout.addStretch()
        self.setLayout(layout)
        self.fontCombo.activated.connect(self.changeFont)
        self.sizeSpinBox.valueChanged.connect(self.changeFont)
    def changeFont(self):
        self.sampleLabel.setFont(
        QFont(self.fontCombo.currentText(), self.sizeSpinBox.value()))
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()