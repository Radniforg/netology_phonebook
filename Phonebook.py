

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

jhon = Contact('Jhon', 'Smith', '+70', email='jhony@smithy.com')
print(jhon)