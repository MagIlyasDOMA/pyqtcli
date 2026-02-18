# argparser.py
import sys

import argparse
import importlib


# Определяем доступный Qt биндинг
def get_qt_binding():
    for binding in ['PySide6', 'PyQt6', 'PyQt5', 'PySide2']:
        try:
            module = importlib.import_module(f"{binding}.QtWidgets")
            return binding, module
        except ImportError:
            continue
    raise ImportError("No Qt binding found")


QT_BINDING, QtWidgets = get_qt_binding()

QApplication = QtWidgets.QApplication
QMessageBox = QtWidgets.QMessageBox
QMainWindow = QtWidgets.QMainWindow
QWidget = QtWidgets.QWidget
QDialog = QtWidgets.QDialog



