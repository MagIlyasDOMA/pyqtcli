from argparse import ArgumentParser
from .QtWidgets import QApplication
from .argparser import CLIMixin


class QCLIApplication(QApplication, CLIMixin):
    def __init__(self, args, **kwargs):
        parser_options = kwargs.pop('parser_options', {})
        super().__init__(args, **kwargs)
        self.parser = ArgumentParser(**parser_options)
