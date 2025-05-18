import datetime

user_score = 10.00  # Глобальная переменная счёта


class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self, value, name):
        timestamp = datetime.datetime.now()
        entry = {
            'дата/время': timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'сумма, руб': value,
            'название': name
        }
        self.entries.append(entry)

    def show_entries(self):
        for entry in self.entries:
            print(entry)


def replenishment():
    """Функция пополнения счёта"""
    global user_score
    pluss = float(input("Пожалуйста, укажите сумму в рублях, на которую желаете пополнить Ваш Счет: "))
    user_score += pluss
    print(f"Ваш Счет пополнен на сумму: {pluss} рублей. Текущий баланс: {user_score:.2f} рублей.")
    return user_score


def purchase(journal):
    """Функция совершения покупки"""
    global user_score
    value = float(input('Введите сумму плановой покупки в рублях: '))
    if value > user_score:
        print(
            "Извините, но Вы не можете позволить себе эту покупку. Сначала необходимо пополнить Ваш счет, не менее чем на: ")
        print(f"{value - user_score:.2f} рублей.")
    else:
        user_score -= value
        name = input('Введите название Вашей покупки: ')
        journal.add_entry(value, name)
        print(f'Ваша покупка "{name}" учтена. Остаток на счете: {user_score:.2f}')
        return user_score


def run_bank_account():
    """Основная функция управления счётом"""
    print("=== Банковский счет ===")
    journal = Journal()

    while True:
        print("*" * 25)
        print("Основное меню программы:")
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            replenishment()
        elif choice == '2':
            purchase(journal)
        elif choice == '3':
            print("История покупок:")
            journal.show_entries()
        elif choice == '4':
            print('Программа завершена')
            break
        else:
            print('Неверный пункт меню!')


# Запуск программы
if __name__ == "__main__":
    run_bank_account()