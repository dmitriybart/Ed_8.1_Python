import view as v
import funcs as f
import data_base as db

def main_menu_prog(choice: int):
    match choice:# match функция которая определяет какое это число и выполняет то, что относится к этому числу
        case 1:
            phone_book = f.get_phone_book()
            v.print_phone_book(phone_book)
        case 2:
            db.load_data_base()
            v.load_succes()
        case 3:
            db.save_data_base()
            v.save_succes()
        case 4:
            contact = v.input_new_contact()
            f.add_contact(contact)
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 0:
            return True # для того чтобы сработал If и мы вышли из программы
while True:
    choice = v.main_menu()
    if main_menu_prog(choice):
        v.log_off()
        break