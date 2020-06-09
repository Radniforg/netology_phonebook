

class Contact:

    def __init__(self, name, surname, number, favorite = False, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.favorite = favorite
        self.add_info_list = []
        for add_info_name, add_info_value in kwargs.items():
            self.add_info_list.append(f'{add_info_name}: {add_info_value}')

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Телефон: {self.number}')
        print(f'В избранных: {self.favorite}')
        print(f'Дополнительная информация:')
        for information in self.add_info_list:
            print(f'        {information}')
        return ''


class PhoneBook:

    contact_list = []

    def __init__(self, name):
        self.name = name
        self.contact_list = []


    def contacts_print(self):
        for contacts in self.contact_list:
            print(contacts)


    def new_contact(self, name, surname, number, favorite = False, **kwargs):
        temp_contact = Contact(name, surname, number, favorite, **kwargs)
        self.contact_list.append(temp_contact)


    def contact_delete(self, number):
        for contacts in self.contact_list:
            if contacts.number == number:
                del(self.contact_list[self.contact_list.index(contacts)])


    def favorite_search(self):
        for contacts in self.contact_list:
            if contacts.favorite:
                print(contacts)


    def contact_search(self, name, surname):
        for contacts in self.contact_list:
            if contacts.name == name and contacts.surname == surname:
                print(contacts)

# jhon = Contact('Jhon', 'Smith', '+70', email='jhony@smithy.com')


testbook = PhoneBook('MyFirstBook')
print(testbook.name)
testbook.new_contact('Jhon', 'Smith', '+70', email='jhony@smithy.com')
testbook.new_contact('Martha', 'Bayne', '+69', True, email='mysonisnot@batman.com')
testbook.contacts_print()
print('---------------')
testbook.favorite_search()
print('---------------')
testbook.contact_search('Jhon', 'Smith')
testbook.contact_delete('+69')
print('---------------')
testbook.contacts_print()
