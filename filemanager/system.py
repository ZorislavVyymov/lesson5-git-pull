import os
import sys
from datetime import datetime

def show_system_info() -> None:
    """Выводит информацию об ОС."""
    print(f"ОС: {sys.platform}")
    print(f"Текущая директория: {os.getcwd()}")
    print(f"Время: {datetime.now()}")

def show_creator() -> None:
    """Выводит информацию о создателе."""
    print("Создатель: Выймов Зорислав")