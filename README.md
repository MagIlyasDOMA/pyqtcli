<a id="doc_en"></a>
# Documentation for the `pyqtcli` Package (PyQt/PySide CLI Integration)
#### [Документация на русском](#doc_ru)

**Version:** 0.1.0  
**Author:** Mag Ilyas DOMA (MagIlyasDOMA)

## Overview

The `pyqtcli` package provides a convenient way to integrate command-line argument (CLI) handling into applications based on the Qt graphical framework (PySide2, PyQt5, PySide6, PyQt6). The main goal is to combine the power of the standard `argparse` module with the ability to display help in a graphical window (QMessageBox), as well as to create a unified application class that combines QApplication and argument parsing logic.

This package will be useful for developers creating GUI utilities that can also be launched with parameters from the command line.

## Installation

The package can be installed from the repository or after it is published on PyPI.

### Basic Installation
```bash
pip install pyqtcli
```

### Installation with Support for Specific Qt Binding
By default, the package will attempt to import any available Qt binding. You can explicitly specify which binding to use by installing the corresponding optional dependencies:

```shell
# For PySide6
pip install pyqtcli[pyside6]

# For PyQt6
pip install pyqtcli[pyqt6]

# For PyQt5
pip install pyqtcli[pyqt5]

# For PySide2
pip install pyqtcli[pyside2]
```

### Dependencies
- `argparse-typing>=0.2.0` (for enhanced typing support in argparse)
- One of the Qt bindings of your choice (installed as an optional dependency).

## Structure and Components
The package consists of several modules:
1. `__init__.py`: Contains the main class `QCLIApplication`.
2. `argparser.py`: Contains the classes `GUIHelpParser` (extending `argparse.ArgumentParser`) and the mixin `CLIMixin`.
3. `QtWidgets.py`: Responsible for dynamic importing and selecting the active Qt binding. Provides a single access point to `QApplication` and `QMessageBox`.
## User Guide
### Module `QtWidgets`
This module is not intended for direct use, but underlies the functioning of the package. It automatically determines the available Qt binding in the following order: `PySide6`, `PyQt6`, `PyQt5`, `PySide2`. If none of them are found, an `ImportError` will be raised. After determining the binding, it makes the classes `QApplication` and `QMessageBox` available.

Class `GUIHelpParser` (from `argparser.py`)
This class inherits from `argparse.ArgumentParser`. Its main feature is the overridden method `print_help()`. When called, it not only outputs the standard help text to the console (`stdout`), but also opens a graphical window (`QMessageBox`) with formatted help.

#### Example usage:
```python
import sys
from pyqtcli.argparser import GUIHelpParser
from pyqtcli.QtWidgets import QApplication

# Create an instance of the Qt application (necessary for QMessageBox to work)
app = QApplication(sys.argv)

# Create the parser
parser = GUIHelpParser(description='My graphical utility')
parser.add_argument('-f', '--file', help='Path to the file')
parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

# If the user requests help (--help), a graphical window will open.
# Otherwise, continue with the workflow.
args = parser.parse_args()

print(f"Loaded file: {args.file}")

# ... rest of the application code
```

### Mixin `CLIMixin` (from `argparser.py`)
This mixin class is designed to add argument parser functionality to any other class. It creates an instance of `GUIHelpParser` within itself and provides proxy methods (`add_argument`, `parse_args`, etc.) to interact with it. This makes it easy to integrate CLI into existing classes, such as the main application window.
#### Mixin Methods:
- `add_arguments()`: Proxy for `parser.add_argument`.
- `add_argument_group()`: Proxy for `parser.add_argument_group`.
- `add_mutually_exclusive_group()`: Proxy for `parser.add_mutually_exclusive_group`.
- `add_subparsers()`: Proxy for `parser.add_subparsers`.
- `parse_args()`: Proxy for `parser.parse_args`.
- `parse_known_args()`: Proxy for `parser.parse_known_args`.
- `messagebox` (property): Returns a `QMessageBox` object used by the parser to display help.

#### Example Usage:
```python
import sys
from pyqtcli.QtWidgets import QMainWindow, QApplication
from pyqtcli.argparser import CLIMixin

class MainWindow(QMainWindow, CLIMixin):
    def __init__(self, *args, **kwargs):
        # Important! Initialize the mixin first to create the parser
        CLIMixin.__init__(self, prog='MyApp', description='Main application window')
        QMainWindow.__init__(self)

        # Set up arguments
        self.add_arguments('--theme', choices=['light', 'dark'], default='light', help='UI theme')
        self.add_arguments('--debug', action='store_true', help='Debug mode')

        # Parse arguments
        self.args = self.parse_args()

        # Apply settings
        self.apply_settings()

    def apply_settings(self):
        print(f"Applying theme: {self.args.theme}")
        if self.args.debug:
            print("Debug mode is enabled")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

## Class `QCLIApplication` (from `__init__.py`)
This class is an all-in-one solution. It inherits from both `QApplication` (from the chosen Qt binding) and `CLIMixin`. This is the ideal way to create a console application with a GUI, where the application itself handles both the Qt event processing loop and the command line argument parsing.
#### Constructor: `__init__(self, argv, *args, **kwargs)`
- `argv`: List of command line arguments (usually `sys.argv`) passed to `QApplication`.
- `*args`, `**kwargs`: Arbitrary arguments passed to the `GUIHelpParser` constructor (via `CLIMixin`).

#### Example usage:
This is the simplest and recommended way to use the package.

```python
import sys
from pyqtcli import QCLIApplication

# Create an application that can parse arguments itself
app = QCLIApplication(sys.argv, description='My super application')

# Add arguments directly to the application
app.add_arguments('-p', '--port', type=int, default=8080, help='Port to listen on')
app.add_arguments('--config', help='Path to configuration file')

# Parse arguments
args = app.parse_args()

print(f"Running on port: {args.port}")
if args.config:
    print(f"Loading configuration from: {args.config}")

# ... create and show main window
# window = MyMainWindow()
# window.show()

# Start the main application loop
sys.exit(app.exec())
```

## Conclusion
The `pyqtcli` package provides an elegant and minimalist way to combine two worlds: command line and graphical interface in Python/Qt applications. It is easy to use, flexible, and automatically adapts to different versions of Qt bindings, making it an excellent choice for a wide range of projects.

---

<a id="doc_ru"></a>
# Документация пакета `pyqtcli` (PyQt/PySide CLI Integration)
#### [Documentation in English](#doc_en)

**Версия:** 0.1.0
**Автор:** Маг Ильяс DOMA (MagIlyasDOMA)

## Обзор

Пакет `pyqtcli` предоставляет удобный способ интеграции обработки аргументов командной строки (CLI) в приложения на базе графического фреймворка Qt (PySide2, PyQt5, PySide6, PyQt6). Основная цель — объединить мощь стандартного модуля `argparse` с возможностью отображения справки в графическом окне (QMessageBox), а также создать единый класс приложения, объединяющий QApplication и логику парсинга аргументов.

Этот пакет будет полезен разработчикам, создающим утилиты с графическим интерфейсом, которые также могут запускаться с параметрами из командной строки.

## Установка

Пакет можно установить из репозитория или после публикации на PyPI.

### Базовая установка
```bash
pip install pyqtcli
```

### Установка с поддержкой конкретного Qt биндинга
По умолчанию пакет попытается импортировать любой доступный Qt биндинг. Вы можете явно указать, какой биндинг использовать, установив соответствующие опциональные зависимости:

```shell
# Для PySide6
pip install pyqtcli[pyside6]

# Для PyQt6
pip install pyqtcli[pyqt6]

# Для PyQt5
pip install pyqtcli[pyqt5]

# Для PySide2
pip install pyqtcli[pyside2]
```

### Зависимости
- `argparse-typing>=0.2.0` (для улучшенной типизации argparse)
- Один из Qt биндингов на ваш выбор (устанавливается как опциональная зависимость).

## Структура и компоненты
Пакет состоит из нескольких модулей:
1. `__init__.py`: Содержит основной класс `QCLIApplication`.
2. `argparser.py`: Содержит классы `GUIHelpParser` (расширяющий `argparse.ArgumentParser`) и миксин `CLIMixin`.
3. `QtWidgets.py`: Отвечает за динамический импорт и выбор активного Qt биндинга. Предоставляет единую точку доступа к `QApplication` и `QMessageBox`.

## Руководство пользователя
### Модуль `QtWidgets`
Этот модуль не предназначен для прямого использования, но лежит в основе работы пакета. Он автоматически определяет доступный Qt биндинг в следующем порядке: `PySide6`, `PyQt6`, `PyQt5`, `PySide2`. Если ни один из них не найден, будет возбуждено исключение `ImportError`. После определения биндинга он делает доступными классы `QApplication` и `QMessageBox`.

Класс `GUIHelpParser` (из `argparser.py`)
Этот класс наследуется от `argparse.ArgumentParser`. Его главная особенность — переопределенный метод `print_help()`. При его вызове помимо стандартного вывода справки в консоль (`stdout`) также открывается графическое окно (`QMessageBox`) с отформатированной справкой.

#### Пример использования:
```python
import sys
from pyqtcli.argparser import GUIHelpParser
from pyqtcli.QtWidgets import QApplication

# Создаем экземпляр приложения Qt (обязательно для работы QMessageBox)
app = QApplication(sys.argv)

# Создаем парсер
parser = GUIHelpParser(description='Моя графическая утилита')
parser.add_argument('-f', '--file', help='Путь к файлу')
parser.add_argument('-v', '--verbose', action='store_true', help='Подробный вывод')

# Если пользователь запросит помощь (--help), откроется графическое окно.
# В противном случае продолжаем работу.
args = parser.parse_args()

print(f"Загружен файл: {args.file}")

# ... остальной код приложения
```

### Миксин `CLIMixin` (из `argparser.py`)
Этот класс-примесь (mixin) предназначен для добавления функциональности парсера аргументов в любой другой класс. Он создает внутри себя экземпляр `GUIHelpParser` и предоставляет прокси-методы (`add_argument`, `parse_args` и т.д.) для работы с ним. Это позволяет легко интегрировать CLI в существующие классы, например, в главное окно приложения.

#### Методы миксина:
- `add_arguments()`: Прокси для `parser.add_argument`.
- `add_argument_group()`: Прокси для `parser.add_argument_group`.
- `add_mutually_exclusive_group()`: Прокси для `parser.add_mutually_exclusive_group`.
- `add_subparsers()`: Прокси для `parser.add_subparsers`.
- `parse_args()`: Прокси для `parser.parse_args`.
- `parse_known_args()`: Прокси для `parser.parse_known_args`.
- `messagebox` (свойство): Возвращает объект `QMessageBox`, используемый парсером для отображения справки.

#### Пример использования:
```python
import sys
from pyqtcli.QtWidgets import QMainWindow, QApplication
from pyqtcli.argparser import CLIMixin

class MainWindow(QMainWindow, CLIMixin):
    def __init__(self, *args, **kwargs):
        # Важно! Сначала инициализируем миксин, чтобы создать парсер
        CLIMixin.__init__(self, prog='MyApp', description='Главное окно приложения')
        QMainWindow.__init__(self)

        # Настраиваем аргументы
        self.add_arguments('--theme', choices=['light', 'dark'], default='light', help='Тема оформления')
        self.add_arguments('--debug', action='store_true', help='Режим отладки')

        # Парсим аргументы
        self.args = self.parse_args()

        # Применяем настройки
        self.apply_settings()

    def apply_settings(self):
        print(f"Применяем тему: {self.args.theme}")
        if self.args.debug:
            print("Включен режим отладки")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

## Класс `QCLIApplication` (из `__init__.py`)
Этот класс является готовым решением "все в одном". Он одновременно наследуется от `QApplication` (из выбранного Qt биндинга) и от `CLIMixin`. Это идеальный способ создать консольное приложение с GUI, где само приложение отвечает и за цикл обработки событий Qt, и за парсинг аргументов командной строки.

#### Конструктор: `__init__(self, argv, *args, **kwargs)`
- `argv`: Список аргументов командной строки (обычно `sys.argv`), передается в `QApplication`.
- `*args`, `**kwargs`: Произвольные аргументы, передаются в конструктор `GUIHelpParser` (через `CLIMixin`).

#### Пример использования:
Это самый простой и рекомендуемый способ использования пакета.

```python
import sys
from pyqtcli import QCLIApplication

# Создаем приложение, которое само умеет парсить аргументы
app = QCLIApplication(sys.argv, description='Мое супер-приложение')

# Добавляем аргументы прямо в приложение
app.add_arguments('-p', '--port', type=int, default=8080, help='Порт для прослушивания')
app.add_arguments('--config', help='Путь к файлу конфигурации')

# Парсим аргументы
args = app.parse_args()

print(f"Запуск на порту: {args.port}")
if args.config:
    print(f"Загрузка конфигурации из: {args.config}")

# ... создание и отображение главного окна
# window = MyMainWindow()
# window.show()

# Запускаем главный цикл приложения
sys.exit(app.exec())
```

## Заключение
Пакет `pyqtcli` предоставляет элегантный и минималистичный способ объединения двух миров: командной строки и графического интерфейса в приложениях на Python/Qt. Он прост в использовании, гибок и автоматически адаптируется под различные версии Qt-биндингов, что делает его отличным выбором для широкого круга проектов.

