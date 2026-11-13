from collections import UserDict


class Field:
    """ Базовий клас для полів запису """
    
    def __init__(self, value):
        self.value = value
        

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Імʼя контакту. Обовʼязкове поле"""
    

class Phone(Field):
    """ Номер телефону з перевіркою формату """
    
    def __init__(self, value):
        # перевірка, чи номер складається з 10 цифр
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain 10 digits.")
        super().__init__(value)
	

class Record:
    """Запис контакту.Імʼя та список телефонів."""
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        

    def add_phone(self, phone):
        """ Додає телефон до запису """
        self.phones.append(Phone(phone))
        
     
    def find_phone(self, phone):
        """ Шукає телефон у записах.Повертає обʼєкт Phone або None """
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    
    def remove_phone(self, phone):
        """ Видаляє номер з запису """
        found = self.find_phone(phone)  # шукає потрібний обʼєкт у списку
        if found:
            self.phones.remove(found)
            
            
    def edit_phone(self, old, new):
        """ Замінює старий номер на новий """
        found = self.find_phone(old)
        if not found:
            raise ValueError("Phone not found.")
        index = self.phones.index(found)
        # новий обʼєкт Phone, щоб спрацювала перевірка на 10 цифр
        self.phones[index] = Phone(new)
    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Адресна книга: імʼя - ключ, Record - значення."""
    
    
    def add_record(self, record):
        """Додає запис до адресної книги"""
        self.data[record.name.value] = record
        
        
    def find(self, name):
        """Шукає запис за імʼям. Повертає Record або None"""
        return self.data.get(name)
    
    
    def delete(self, name):
        """ Видаляє запис за імʼям"""
        if name in self.data:
            del self.data[name] 
            

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону в записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")