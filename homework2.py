def print_params(a=36.6, b='BMW', c=True):  # определение функции
    print(a, b, c)  # вывод параметров


print_params()  # вызов функции с параметрами по умолчанию
print_params(a=38.0)  # вывод с параметром "a"
print_params(a=38.0, b='HONDA')  # вывод функции с параметрами "a" и "b"
print_params(c=False)   # вывод функции с параметром "с"
print_params(b=25)  # вывод функции с параметром "b"
print_params(c=[1, 2, 3])  # вывод функции с параметром "с"
print()
values_list = ['alpha', (5, 4, 3, 2, 1), True]  # определение переменной "список"
values_dict = {'a': 40.4, 'b': 'Mitsubishi', 'c': 'Oh, my God!'}  # определение переменной "словарь"
print_params(*values_list)  # вывод функции с распаковкий параметров списка
print_params(**values_dict)  # вывод функции с распаковкий параметров словаря
print()
values_list_2 = [[7, 77, 777], 'river']  # определение переменной "список"
print_params(*values_list_2, 42)  # вывод функции с распаковкий параметров списка и параметром "a"
