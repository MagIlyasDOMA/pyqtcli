import sys
from argparse import ArgumentParser, _FormatterClass
from typing import Final, Sequence, Any
from ._widgets import QApplication
from .argparser import CLIMixin, GUIHelpParser

__version__: Final[str] = '1.0.0'
__all__: Final[str] = ['QCLIApplication', 'CLIMixin', 'GUIHelpParser']


class QCLIApplication(QApplication, CLIMixin):
    if sys.version_info >= (3, 14):
        def __init__(
            self,
            argv: Sequence[str],
            prog: str | None = None,
            usage: str | None = None,
            description: str | None = None,
            epilog: str | None = None,
            parents: Sequence[ArgumentParser] = [],
            formatter_class: _FormatterClass = ...,
            prefix_chars: str = "-",
            fromfile_prefix_chars: str | None = None,
            argument_default: Any = None,
            conflict_handler: str = "error",
            add_help: bool = True,
            allow_abbrev: bool = True,
            exit_on_error: bool = True,
            *,
            suggest_on_error: bool = False,
            color: bool = False,
        ) -> None: ...
    else:
        def __init__(
            self,
            argv: Sequence[str],
            prog: str | None = None,
            usage: str | None = None,
            description: str | None = None,
            epilog: str | None = None,
            parents: Sequence[ArgumentParser] = [],
            formatter_class: _FormatterClass = ...,
            prefix_chars: str = "-",
            fromfile_prefix_chars: str | None = None,
            argument_default: Any = None,
            conflict_handler: str = "error",
            add_help: bool = True,
            allow_abbrev: bool = True,
            exit_on_error: bool = True,
        ) -> None: ...
