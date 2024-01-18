import sys

sys.path.append("../")
import unittest
from gui.main import Window
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)


class WindowTest(unittest.TestCase):
    window = None

    def setUp(self):
        self.window = Window()

    def sets(self, a, b, c):
        self.window.lineEdit1.setText(a)
        self.window.lineEdit2.setText(b)
        self.window.lineEdit3.setText(c)
        self.window.btn1.click()

    def test_check_string(self):
        self.assertEqual(self.window.main_text.text(), "Введите три стороны треугольника")
        self.assertEqual(self.window.result_text.text(), "Результат расчета")
        self.assertEqual(self.window.btn1.text(), "Выполнить проверку")
        self.assertEqual(self.window.windowTitle(), "Расчет треугольника")

    def test_triangle_false(self):
        self.sets("1", "2", "3")
        self.assertEqual(self.window.label.text(), "Треугольник не существует")

    def test_triangle_true(self):
        self.sets("2", "5", "6")
        self.assertEqual(self.window.label.text(), "Треугольник существует")

    def test_negative_number(self):
        self.sets("-1", "5", "6")
        self.assertEqual(self.window.label.text(), "Треугольник не существует")

    def test_entering_letters(self):
        self.sets("c", "5", "6")
        self.assertEqual(self.window.label.text(), "Введите корректные значения")

    def test_caps_letters(self):
        self.sets("C", "5", "6")
        self.assertEqual(self.window.label.text(), "Введите корректные значения")

    def test_empty_value(self):
        self.sets("", "", "6")
        self.assertEqual(self.window.label.text(), "Введите корректные значения")

    def test_whitespace(self):
        self.sets("6", " ", "6")
        self.assertEqual(self.window.label.text(), "Введите корректные значения")

    def test_simbols(self):
        self.sets("7", "+", "6")
        self.assertEqual(self.window.label.text(), "Введите корректные значения")

    def test_kirill(self):
        self.sets("7", "щ", "6")
        self.assertEqual(self.window.label.text(), "Введите корректные значения")
