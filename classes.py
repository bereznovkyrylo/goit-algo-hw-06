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
        for phone in self.phones:
            if phone.value==old_phone:
                phone.value=new_phone
                break
        else:
            raise ValueError
    def find_phone(self,searched_phone):
        for phone in self.phones:
            if phone.value==searched_phone:
                return phone
        else:
            return None
    def remove_phone(self,phone):
        self.phones=filter(lambda x :x.value!=phone,self.phones) 


    def __str__(self): 
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)};"


class AddressBook(UserDict):
    def add_record(self,record:Record):
        name=record.name.value
        self.data[name]=record
    def find(self,name):
        for key in self.data:
            if key==name:
                return self.data[key]
        return None
    def delete(self,name):
        data=self.data 
        self.data={key:data[key] for key in data if key!=name}


    def __str__(self):
        return '\n'.join(f'{str(value)}' for value in self.data.values())



class Field():
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    ...
class Phone(Field):
    def __init__(self,phone:str):
        if len(phone)!=10:
            raise ValueError
        super().__init__(phone)

