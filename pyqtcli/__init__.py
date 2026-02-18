from .QtWidgets import QApplication
from .argparser import CLIMixin, GUIHelpParser

__version__ = '0.1.0'


class QCLIApplication(QApplication, CLIMixin):
    def __init__(self, argv, *args, **kwargs):
        CLIMixin.__init__(self, *args, **kwargs)
        QApplication.__init__(self, argv)
