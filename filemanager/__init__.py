"""Инициализация пакета filemanager."""

from .core import (
    create_folder,
    delete_file_or_folder,
    copy_file_or_folder,
    list_directory_contents,
    list_folders_only,
    list_files_only,
    change_working_directory,
)

from .system import (
    show_system_info,
    show_creator,
)

from .games.victory import play_victory
from .games.bank import run_bank_account

__all__ = [
    'create_folder',
    'delete_file_or_folder',
    'copy_file_or_folder',
    'list_directory_contents',
    'list_folders_only',
    'list_files_only',
    'change_working_directory',
    'show_system_info',
    'show_creator',
    'play_victory',
    'run_bank_account',
]