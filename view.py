def main_menu():
    print('\n\t\t*****Главное меню*****')
    print('''
            1 - Вывести телефонную книгу
            2 - Открыть файл телефонной книги
            3 - Сохранить файл телефонной книги
            4 - Добавить контакт
            5 - Изменить контакт
            6 - Удалить контакт
            7 - Найти контакт
            8 - Импортировать файл в телефонную книгу
            9 - экспортировать телефонную книгу
            0 - Выход\n''')
    return choice_main_menu()

def choice_main_menu():
    while True:
        try: # Метод, который при сработывании ошибки переходит к Except (вроде, это надо изучить)
            choice = int(input('Выберите пункт меню: '))
            print()
            if choice in range(0, 10):#Проверяем число в диапазоне нашего меню или нет
                return choice
            else:
                print('Такого пункта нет, повторите попытку')
        except:
            print('Ошибка ввода! Некорректные данные!')


def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1): #Энумирейт присваивает id к нашему справочнику
            print(id, *contact)# т.к. contact у нас иет списком, то мы ео расскрываем через (*)
    else:
        print('Телефонная книга пустая или не загружена')


def log_off():
    print('До свидания, ждем тебя снова =)')

def load_succes():
    print('Телефонная книга загружена')

def save_succes():
    print('Телефонная книга сохранена')

def remove_succes():
    print('\nКонтакт удален')

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return [name, phone, comment]

def input_remove_contact():
    id = int(input('Введите ID контакта, который желаете удалить: '))
    return id

