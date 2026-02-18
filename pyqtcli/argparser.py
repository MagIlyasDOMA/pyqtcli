import argparse
from .QtWidgets import QT_BINDING, QMessageBox


class GUIHelpParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.messagebox = self._init_messagebox()

    def _init_messagebox(self):
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Help")

        # Совместимость с разными версиями Qt
        if QT_BINDING in ['PySide6', 'PyQt6']:
            messagebox.setIcon(QMessageBox.Icon.Information)
        else:  # PyQt5, PySide2
            messagebox.setIcon(QMessageBox.Information)

        messagebox.setText(self.format_help())
        return messagebox

    def print_help(self, file=None):
        super().print_help(file)
        try:
            self.messagebox.exec()
        except AttributeError:
            self.messagebox.exec_()


class CLIMixin:
    def __init__(self, *args, **kwargs):
        self.parser = GUIHelpParser(*args, **kwargs)

    def add_arguments(self, *name_or_flags, **kwargs):
        return self.parser.add_argument(*name_or_flags, **kwargs)

    def add_argument_group(self, *args, **kwargs):
        return self.parser.add_argument_group(*args, **kwargs)

    def add_mutually_exclusive_group(self, *args, **kwargs):
        return self.parser.add_mutually_exclusive_group(*args, **kwargs)

    def add_subparsers(self, *args, **kwargs):
        return self.parser.add_subparsers(*args, **kwargs)

    def parse_args(self, *args, **kwargs):
        return self.parser.parse_args(*args, **kwargs)

    def parse_known_args(self, *args, **kwargs):
        return self.parser.parse_known_args(*args, **kwargs)

    @property
    def messagebox(self):
        return self.parser.messagebox
