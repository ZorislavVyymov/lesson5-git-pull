from filemanager import (
    create_folder,
    delete_file_or_folder,
    copy_file_or_folder,
    list_directory_contents,
    list_folders_only,
    list_files_only,
    show_system_info,
    show_creator,
    play_victory,
    run_bank_account,
    change_working_directory,
)

def main():
    while True:
        print("\n=== Консольный файловый менеджер ===")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Данные по создателю программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            folder_name = input("Введите название папки: ")
            create_folder(folder_name)
        elif choice == "2":
            del_name = input("Введите название папки: ")
            delete_file_or_folder(del_name)
        elif choice == "3":
            copy_file_or_folder()
        elif choice == "4":
            list_directory_contents()
        elif choice == "5":
            list_folders_only()
        elif choice == "6":
            list_files_only()
        elif choice == "7":
            show_system_info()
        elif choice == "8":
            show_creator()
        elif choice == "9":
            play_victory()
        elif choice == "10":
            run_bank_account()
        elif choice == "11":
            change_working_directory()
        elif choice == "12":
            print('Программа завершена!')
            break
        else:
            print('Неверный пункт меню!')


if __name__ == "__main__":
    main()