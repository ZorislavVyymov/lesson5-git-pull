import os
import shutil

def create_folder(folder_name: str) -> None:
    """Создает папку в текущей директории."""
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Папка '{folder_name}' создана.")
    else:
        print(f"Папка '{folder_name}' уже существует.")

def delete_file_or_folder(name: str) -> None:
    """Удаляет файл или папку."""
    if os.path.exists(name):
        if os.path.isfile(name):
            os.remove(name)
            print(f"Файл '{name}' удалён.")
        else:
            os.rmdir(name)
            print(f"Папка '{name}' удалена.")
    else:
        print(f"Файл/папка '{name}' не найдена.")

# Аналогично остальные функции (copy, list и т.д.)
def copy_file_or_folder():
    src = input("Введите название исходного файла/папки: ")
    dst = input("Введите новое название: ")
    if os.path.exists(src):
        if os.path.isfile(src):
            shutil.copy(src, dst)
            print(f"Файл '{src}' скопирован в '{dst}'.")
        else:
            shutil.copytree(src, dst)
            print(f"Папка '{src}' скопирована в '{dst}'.")
    else:
        print(f"Файл/папка '{src}' не найдена.")

def list_directory_contents():
    print("\nСодержимое рабочей директории:")
    for item in os.listdir():
        print(item)

def list_folders_only():
    print("\nТолько папки:")
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)

def list_files_only():
    print("\nТолько файлы:")
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)

def play_victory():
    try:
        import victory
        victory.run_quiz()  # Предполагается, что функция запуска викторины называется `run_quiz`
    except ImportError:
        print("Модуль 'victory.py' не найден!")

def run_bank_account():
    try:
        import bank
        bank.run_bank()  # Предполагается, что функция управления счётом называется `run_bank`
    except ImportError:
        print("Модуль 'bank.py' не найден!")

def change_working_directory():
    new_dir = input("Введите новый путь (абсолютный или относительный): ")
    if os.path.exists(new_dir):
        os.chdir(new_dir)
        print(f"Текущая директория изменена на: {os.getcwd()}")
    else:
        print("Указанный путь не существует!")
