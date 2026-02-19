<a id="doc_en"></a>
# Pyqtcli documentation (PyQt/PySide CLI Integration)
#### [Документация на русском](#doc_ru)

**PyQtCLI** is a Python package that simplifies integrating command-line argument parsing into Qt-based GUI applications (PySide/PyQt). It allows you to easily combine the standard `argparse` module with the ability to display help messages in a graphical window (`QMessageBox`).

## Features
- **Backend Flexibility:** Automatically detects the available Qt binding (`PySide6`, `PyQt6`, `PyQt5`, `PySide2`).
- **Graphical Help:** The `GUIHelpParser` class overrides the help output (`-h`, `--help`), displaying it not only in the console but also in a pop-up `QMessageBox` window.
- **Convenient Mixin:** The `CLIMixin` class provides all the methods of `argparse.ArgumentParser` (`add_argument`, `parse_args`, etc.) for easy addition to your classes.
- **Ready-to-Use Integration:** The `QCLIApplication` class is a ready-to-use subclass of `QApplication` with the `CLIMixin` functionality already built-in.
- **Type Hints:** Includes `.pyi` files for better autocompletion and type checking support in modern IDEs.

## Installation
You can install the package directly from the repository or from PyPI after publication (replace with the actual command):

```shell
# From repository
pip install git+https://github.com/MagIlyasDOMA/pyqtcli.git

# Or after publication (example)
pip install pyqtcli
```

The package does not automatically install a specific Qt library. You need to install one of the supported bindings yourself:

```shell
# For example, for PySide6
pip install pyqtcli[pyside6]

# Or for PyQt5
pip install pyqtcli[pyqt5]
```

## Usage
### Quick Start with QCLIApplication
The easiest way to create an application with command-line argument support is to use the ready-made `QCLIApplication` class.

```python
import sys
from pyqtcli import QCLIApplication
from PySide6.QtWidgets import QMainWindow, QLabel # Example for PySide6

# Create an application instance, passing the command-line arguments
# All additional parameters (prog, description, etc.) are passed to the parser.
app = QCLIApplication(
    sys.argv,
    description="My Super Application",
    epilog="Example of using QCLIApplication"
)

# Add your own arguments, just like in standard argparse
app.add_argument("-f", "--file", help="Path to the file to open")
app.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

# Parse the arguments. Help (-h) will automatically be displayed in a graphical window.
args = app.parse_args()

# --- Standard Qt application code follows ---
window = QMainWindow()
if args.file:
    window.setCentralWidget(QLabel(f"Opened file: {args.file}"))
else:
    window.setCentralWidget(QLabel("Hello, world!"))
window.show()

sys.exit(app.exec())
```

### Using CLIMixin in Your Own QApplication Class
If you need more control or want to add parsing functionality to your own application class, use `CLIMixin`.

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from pyqtcli import CLIMixin

class MyApp(QApplication, CLIMixin):
    def __init__(self, argv):
        # First, initialize the mixin with parser parameters
        CLIMixin.__init__(self, description="My Custom Application")
        # Then initialize QApplication
        QApplication.__init__(self, argv)

        # Add your own arguments
        self.add_argument("--debug", action="store_true", help="Enable debug mode")

        # Parse the arguments
        self.args = self.parse_args()

        if self.args.debug:
            print("Debug mode enabled")

# Run the application
if __name__ == "__main__":
    app = MyApp(sys.argv)

    window = QMainWindow()
    window.setCentralWidget(QLabel("Application Window"))
    window.show()

    sys.exit(app.exec())
```

### Using GUIHelpParser Directly
You can use the graphical parser directly, for example, to create a standalone tool.

```python
import sys
from PySide6.QtWidgets import QApplication
from pyqtcli.argparser import GUIHelpParser

# Create the parser
app = QApplication(sys.argv)
parser = GUIHelpParser(prog="tool.py", description="Tool with GUI help")
parser.add_argument("-o", "--output", help="File to save the result")

# When parse_args() is called, help will be shown in a window
# if the -h or --help arguments are passed.
# Otherwise, parsing proceeds as usual.
args = parser.parse_args()
print(args)
```

Package Structure
- `__init__.py`: The main module, exporting the `QCLIApplication`, `CLIMixin`, and `GUIHelpParser` classes.
- `_widgets.py`: An internal module for automatically selecting and importing the required Qt binding.
- `argparser.py`: Contains the `GUIHelpParser` (parser with graphical help) and `CLIMixin` (mixin for adding a parser to any class) classes.

---

<a id="doc_ru"></a>
# Документация пакета pyqtcli (PyQt/PySide CLI Integration)
#### [Documentation in English](#doc_en)

**PyQtCLI** — это пакет для Python, который упрощает интеграцию парсинга аргументов командной строки в приложениях с графическим интерфейсом на базе Qt (PySide/PyQt). Он позволяет легко комбинировать стандартный `argparse` с возможностью отображения справки в графическом окне (`QMessageBox`).

## Возможности
- **Гибкость бэкенда:** Автоматически определяет доступную библиотеку Qt (`PySide6`, `PyQt6`, `PyQt5`, `PySide2`).
- **Графическая справка:** Класс `GUIHelpParser` переопределяет вывод справки (`-h`, `--help`), отображая её не только в консоли, а в всплывающем окне `QMessageBox`.
- **Удобный миксин:** Класс `CLIMixin` предоставляет все методы `argparse.ArgumentParser` (`add_argument`, `parse_args` и т.д.) для простого добавления в ваши классы.
- **Готовая интеграция:** Класс `QCLIApplication` является готовым к использованию наследником `QApplication` с уже встроенным функционалом `CLIMixin`.
- **Типизация:** В комплекте идут `.pyi` файлы для лучшей поддержки автодополнения и проверки типов в современных IDE.

## Установка
Установить пакет можно напрямую из репозитория или после публикации из PyPI (замените на актуальную команду):

```shell
# Из репозитория
pip install git+https://github.com/MagIlyasDOMA/pyqtcli.git

# Или после публикации (пример)
pip install pyqtcli
```

Пакет не устанавливает автоматически конкретную Qt-библиотеку. Вам необходимо установить одну из поддерживаемых самостоятельно:

```shell
# Например, для PySide6
pip install pyqtcli[pyside6]

# Или для PyQt5
pip install pyqtcli[pyqt5]
```

## Использование
### Быстрый старт с QCLIApplication
Самый простой способ создать приложение с поддержкой аргументов командной строки — использовать готовый класс `QCLIApplication`.

```python
import sys
from pyqtcli import QCLIApplication
from PySide6.QtWidgets import QMainWindow, QLabel # Пример для PySide6

# Создаем экземпляр приложения, передавая аргументы командной строки
# Все дополнительные параметры (prog, description и т.д.) уходят в парсер.
app = QCLIApplication(
    sys.argv,
    description="Мое супер приложение",
    epilog="Пример использования QCLIApplication"
)

# Добавляем свои аргументы, как в обычном argparse
app.add_argument("-f", "--file", help="Путь к файлу для открытия")
app.add_argument("-v", "--verbose", action="store_true", help="Подробный вывод")

# Парсим аргументы. Справка (-h) автоматически отобразится в графическом окне.
args = app.parse_args()

# --- Здесь стандартный код Qt приложения ---
window = QMainWindow()
if args.file:
    window.setCentralWidget(QLabel(f"Открыт файл: {args.file}"))
else:
    window.setCentralWidget(QLabel("Привет, мир!"))
window.show()

sys.exit(app.exec())
```

### Использование CLIMixin в своем классе QApplication
Если вам нужно больше контроля или вы хотите добавить функционал парсинга в свой собственный класс приложения, используйте `CLIMixin`.

```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from pyqtcli import CLIMixin

class MyApp(QApplication, CLIMixin):
    def __init__(self, argv):
        # Сначала инициализируем миксин с параметрами парсера
        CLIMixin.__init__(self, description="Мое кастомное приложение")
        # Затем инициализируем QApplication
        QApplication.__init__(self, argv)

        # Добавляем свои аргументы
        self.add_argument("--debug", action="store_true", help="Включить режим отладки")

        # Парсим аргументы
        self.args = self.parse_args()

        if self.args.debug:
            print("Отладка включена")

# Запуск приложения
if __name__ == "__main__":
    app = MyApp(sys.argv)

    window = QMainWindow()
    window.setCentralWidget(QLabel("Окно приложения"))
    window.show()

    sys.exit(app.exec())
```

### Использование GUIHelpParser напрямую
Вы можете использовать графический парсер напрямую, например, для создания отдельного инструмента.

```python
import sys
from PySide6.QtWidgets import QApplication
from pyqtcli.argparser import GUIHelpParser

# Создаем парсер
app = QApplication(sys.argv)
parser = GUIHelpParser(prog="tool.py", description="Инструмент с GUI-справкой")
parser.add_argument("-o", "--output", help="Файл для вывода результата")

# При вызове parse_args() справка будет показана в окне,
# если переданы аргументы -h или --help.
# В противном случае парсинг пройдет как обычно.
args = parser.parse_args()
print(args)
```

## Структура пакета
- `__init__.py`: Основной модуль, экспортирующий классы `QCLIApplication`, `CLIMixin` и `GUIHelpParser`.
- `_widgets.py`: Внутренний модуль для автоматического выбора и импорта нужного Qt биндинга.
- `argparser.py`: Содержит классы `GUIHelpParser` (парсер с графической справкой) и `CLIMixin` (миксин для добавления парсера в любой класс).
