import sys
from argparse import ArgumentParser, _N, Namespace, _SubParsersAction, Action, _FormatterClass, _ArgumentParserT, \
    _ActionTyping, _NargsType, _ActionType, _T, _ArgumentGroup, _MutuallyExclusiveGroup
from typing import Sequence, Any, overload, Optional, Iterable, Final
from ._widgets import QMessageBox

__all__: Final[str] = ['GUIHelpParser', 'CLIMixin']


class GUIHelpParser(ArgumentParser):
    def __init__(self, *args, **kwargs) -> None:
        self._messagebox: QMessageBox = ...
        self.exit_on_help: bool = ...

    def _init_messagebox_lazy(self) -> QMessageBox: ...

    def print_help(self, file=None) -> None: ...

    @property
    def messagebox(self) -> QMessageBox: ...

class CLIMixin:
    if sys.version_info >= (3, 14):
        def __init__(
                self,
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
                exit_on_help: bool = True
        ) -> None:
            self.parser: GUIHelpParser = ...
    else:
        def __init__(
                self,
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
                exit_on_help: bool = True
        ) -> None:
            self.parser: GUIHelpParser = ...

    def add_argument(
        self,
        *name_or_flags: str,
        # str covers predefined actions ("store_true", "count", etc.)
        # and user registered actions via the `register` method.
        action: _ActionTyping = ...,
        # more precisely, Literal["?", "*", "+", "...", "A...", "==SUPPRESS=="],
        # but using this would make it hard to annotate callers that don't use a
        # literal argument and for subclasses to override this method.
        nargs: Optional[_NargsType] = None,
        const: Any = ...,
        default: Any = ...,
        type: _ActionType = ...,
        choices: Iterable[_T] | None = ...,
        required: bool = ...,
        help: str | None = ...,
        metavar: str | tuple[str, ...] | None = ...,
        dest: str | None = ...,
        version: str = ...,
        **kwargs: Any,
    ) -> Action: ...

    def add_argument_group(
        self,
        title: str | None = None,
        description: str | None = None,
        *,
        prefix_chars: str = ...,
        argument_default: Any = ...,
        conflict_handler: str = ...,
    ) -> _ArgumentGroup: ...
    def add_mutually_exclusive_group(self, *, required: bool = False) -> _MutuallyExclusiveGroup: ...

    @overload
    def parse_args(self, args: Sequence[str] | None = None, namespace: None = None) -> Namespace: ...
    @overload
    def parse_args(self, args: Sequence[str] | None, namespace: _N) -> _N: ...
    @overload
    def parse_args(self, *, namespace: _N) -> _N: ...

    @overload
    def add_subparsers(
            self: _ArgumentParserT,
            *,
            title: str = "subcommands",
            description: str | None = None,
            prog: str | None = None,
            action: type[Action] = ...,
            option_string: str = ...,
            dest: str | None = None,
            required: bool = False,
            help: str | None = None,
            metavar: str | None = None,
    ) -> _SubParsersAction[_ArgumentParserT]: ...
    @overload
    def add_subparsers(
            self,
            *,
            title: str = "subcommands",
            description: str | None = None,
            prog: str | None = None,
            parser_class: type[_ArgumentParserT],
            action: type[Action] = ...,
            option_string: str = ...,
            dest: str | None = None,
            required: bool = False,
            help: str | None = None,
            metavar: str | None = None,
    ) -> _SubParsersAction[_ArgumentParserT]: ...

    @overload
    def parse_known_args(self, args: Sequence[str] | None = None, namespace: None = None) -> tuple[
        Namespace, list[str]]: ...
    @overload
    def parse_known_args(self, args: Sequence[str] | None, namespace: _N) -> tuple[_N, list[str]]: ...
    @overload
    def parse_known_args(self, *, namespace: _N) -> tuple[_N, list[str]]: ...

    @property
    def messagebox(self) -> QMessageBox:
        return self.parser.messagebox
