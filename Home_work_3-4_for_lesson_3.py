"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
"""
def thesaurus(*names):
    dict_of_names = {}
    for name in names:
        if name[0] not in dict_of_names.keys():
            dict_of_names[name[0]] = []
            dict_of_names[name[0]].append(name)
        else:
            dict_of_names[name[0]].append(name)
    return dict_of_names
print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Афанасий', 'Авдотья'))

"""
4. 4* (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
в котором ключи — первые буквы фамилий,
а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
"""
def thesaurus(*full_names):
    dict_of_surnames = {}
    for name_surname in full_names:
        name, surname = name_surname.split()
        dict_of_surnames[surname[0]] = dict_of_surnames.setdefault(surname[0], {})
        #print(dict_of_surnames[surname[0]])
        dict_of_surnames[surname[0]][name[0]] = dict_of_surnames[surname[0]].setdefault(name[0], []) + [name_surname]
    return dict_of_surnames
print(thesaurus("Иван Сергеев", "Инна Серова",
                "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

