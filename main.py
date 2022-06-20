import re
import csv
from pprint import pprint


def open_file(file):
    """открытие файла"""
    with open(file) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def regular(contacts,pattern,sub):
    """приведение записей к определенному формату"""
    new_list = list()
    for contact in contacts:
        full_name = ' '.join(contact[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], contact[3], contact[4],
        re.sub(pattern, sub, contact[5]), contact[6]]
        new_list.append(result)
    return new_list

def delete_dublicates(contacts):
    """удаление дублирующих записей"""
    contacts_dict = dict()
    for contact in contacts:
        if contact[0] in contacts_dict:
            contact_value = contacts_dict[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            contacts_dict[contact[0]] = contact
    return list(contacts_dict.values())

def write_file(contacts_list):
    """запись файла в формате CSV"""
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
    return


if __name__ == '__main__':
    data_file = "phonebook_raw.csv"
    pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
    sub = r"+7(\2)-\3-\4-\5 \6\7"
    new_list = open_file(data_file)
    new_regular = regular(new_list,pattern,sub)
    new_union = delete_dublicates(new_regular)
    write_file(new_union)
