import funcs as f

path = 'phone_book.txt'

def load_data_base():
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = file.readlines()
    f.set_phone_book(str_to_list(phone_book))

def str_to_list(phone_book: list):
    new_phone_book = []
    for contact in phone_book:
        new_phone_book.append(contact.strip().split(';'))#strip - подчищает слева и справа от лишнего(\n, пробелы и тд), выводит все в строки, как в файле, а split мы разделяем на строки и формирует в списки со строками
    return new_phone_book