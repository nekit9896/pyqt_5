import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Расчет треугольника")
        self.setGeometry(600, 450, 450, 600)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Введите три стороны треугольника")
        self.main_text.move(100, 50)
        self.main_text.adjustSize()

        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setGeometry(QtCore.QRect(100, 70, 200, 26))
        self.lineEdit1.setObjectName("textEdit")

        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(100, 100, 200, 26))
        self.lineEdit2.setObjectName("textEdit")

        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit3.setGeometry(QtCore.QRect(100, 130, 200, 26))
        self.lineEdit3.setObjectName("textEdit")

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(100, 160)
        self.btn1.setText("Выполнить проверку")
        self.btn1.setFixedWidth(200)
        self.btn1.clicked.connect(self.collect_sides)

        self.result_text = QtWidgets.QLabel(self)
        self.result_text.setText("Результат расчета")
        self.result_text.move(100, 220)
        self.result_text.adjustSize()

        self.label = QtWidgets.QLineEdit(self)
        self.label.setGeometry(QtCore.QRect(100, 240, 200, 26))
        self.label.setObjectName("textEdit")

    @QtCore.pyqtSlot()
    def collect_sides(self):
        try:
            a = float(self.lineEdit1.text())
            b = float(self.lineEdit2.text())
            c = float(self.lineEdit3.text())
            self.proverka(a, b, c)
        except ValueError:
            self.label.setText("Введите корректные значения")
        except TypeError:
            self.label.setText("Введите корректные значения")
        except OverflowError:
            self.label.setText("Введите корректные значения")

    def proverka(self, a, b, c):
        if a > 0 and b > 0 and c > 0 and (a + b > c) and (b + c > a) and (a + c > b):
            self.label.setText("Треугольник существует")
        else:
            self.label.setText("Треугольник не существует")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
