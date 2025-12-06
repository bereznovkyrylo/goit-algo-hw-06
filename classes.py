"""
Field: Базовий клас для полів запису.
Name: Клас для зберігання імені контакту. Обов'язкове поле.
Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
AddressBook: Клас для зберігання та управління записами.
"""
from collections import UserDict


class Record():
    def __init__(self,name):
        self.name=Name(name)
        self.phones=[]

    def add_phone(self,phone:str)->None:
        self.phones.append(Phone(phone))

    def edit_phone(self,old_phone,new_phone):
        
        searched_phone=self.find_phone(old_phone)

        if searched_phone is None:
            raise ValueError('Phone not found')
        if not searched_phone.is_valid_phone(new_phone):
            raise ValueError('Phone number is not valid')
        
        searched_phone.value=new_phone

        
    def find_phone(self,searched_phone):
        for phone in self.phones:
            if phone.value==searched_phone:
                return phone
        else:
            return None
        
    def remove_phone(self,phone):
        searched_phone=self.find_phone(phone)
        if searched_phone is not None:
            self.data.pop(searched_phone)
        else:
            raise ValueError('Phone not found')

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)};"



class AddressBook(UserDict):

    def add_record(self,record:Record):
        name=record.name.value
        self.data[name]=record

    def find(self,name):
        return self.data.get(name)
    
    def delete(self,name):
        searched_address=self.find(name)

        if searched_address is not None:
            self.data.pop(name)
        else :
            raise ValueError('No such address')

    def __str__(self):
        return '\n'.join(f'{str(value)}' for value in self.data.values())



class Field():

    def __init__(self,value):
        self.value=value

    def __str__(self):
        return str(self.value)

class Name(Field):
    ...

class Field():

    def __init__(self,value):
        self.value=value

    def __str__(self):
        return str(self.value)
class Phone(Field):
    phone_number_length=10

    def __init__(self,phone:str): 
        if self.is_valid_phone(phone):
            super().__init__(phone)
        else:    
            raise ValueError('Wrong phone number')
        
    def is_valid_phone(cls,phone:str)->bool:
        return len(phone)==cls.phone_number_length and phone.isdigit()

