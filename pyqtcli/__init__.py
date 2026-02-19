from ._widgets import QApplication
from .argparser import CLIMixin, GUIHelpParser

__version__ = '0.1.1'
__all__ = ['QCLIApplication', 'CLIMixin', 'GUIHelpParser']


class QCLIApplication(QApplication, CLIMixin):
    def __init__(self, argv, *args, **kwargs):
        QApplication.__init__(self, argv)
        CLIMixin.__init__(self, *args, **kwargs)
