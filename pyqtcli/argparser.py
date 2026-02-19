import argparse, sys
from ._widgets import QT_BINDING, QMessageBox

__all__ = ['GUIHelpParser', 'CLIMixin']


class GUIHelpParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._messagebox = None  # Не создаем сразу
        self.exit_on_help = kwargs.pop('exit_on_help', True)

    def _init_messagebox_lazy(self):
        """Ленивое создание QMessageBox"""
        if self._messagebox is None:
            self._messagebox = QMessageBox()
            self._messagebox.setWindowTitle("Help")

            # Совместимость с разными версиями Qt
            if QT_BINDING in ['PySide6', 'PyQt6']:
                self._messagebox.setIcon(QMessageBox.Icon.Information)
            else:  # PyQt5, PySide2
                self._messagebox.setIcon(QMessageBox.Information)

            self._messagebox.setText(self.format_help())

        return self._messagebox

    def print_help(self, file=None):
        super().print_help(file)
        try:
            self._init_messagebox_lazy().exec()
        except AttributeError:
            self._init_messagebox_lazy().exec_()
        if self.exit_on_help: sys.exit(0)

    @property
    def messagebox(self):
        return self._init_messagebox_lazy()


class CLIMixin:
    def __init__(self, *args, **kwargs):
        self.parser = GUIHelpParser(*args, **kwargs)

    def add_argument(self, *name_or_flags, **kwargs):
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