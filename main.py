# Name: Generate structure ID:6 Difficulty: B Propose: TDY
# Creati un script care primeste de la linia de comanda un path catre un director si un fisier
# JSON. In fisierul JSON se afla un dictionar in care se afla o structura de directoare si fisiere
# astfel: fiecare cheie care are ca valoare un dictionar este un director iar dictionarul contintul,
# iar fiecare cheie care are ca valoare un string reprezinta un fisier iar string-ul respectiv este
# continutul fisierului. Scriptul va crea in folderul dat ca argument directoarele si fisierele
#
# conform dictionarului din JSON.
# INPUT: create_structure.py root_folder_path structure_json_file_path
# Exemplu de dictionar:
# {"dir1" : {"dir2": {"file1": "continut1", "file2": "continut2"}, "file3": "continut3"}, "file4": "continut4"}
# OUTPUT:
# root_folder
# ---dir1
# ------dir2
# ---------file1: continut1
# ---------file2: continut2
# ------file3: continut3
# ---file4: continut4


# TODO:
# - get main arguments from console
# - test on linux when fix are done
# - test if gitignore doesn't ignore important files

import json
import os


def get_json_text(path_json):
    if not(os.path.exists(path_json)):
        raise Exception("Path to json '" + path_json + "' doesn't exit.")

    if not(os.path.isfile(path_json)):
        raise Exception("Path to json '" + path_json + "' does NOT point to a file.")

    f = open(path_json, "r")
    return f.read()


def create_file(path, content):
    f = open(path, 'w+')
    f.write(content)
    f.close()

    print("Created/overwritten file " + path + ", with content '" + content + "'")


def create_folder(path):
    if os.path.exists(path) and os.path.isdir(path):
        print("Folder already exists: " + path)
        return

    if os.path.exists(path) and not(os.path.isdir(path)):
        os.remove(path)
        print("Folder name is already used for a non-folder... so the respective entity was deleted: " + path)

    os.mkdir(path)
    print("Folder created " + path)


def create_structure(root, obj):
    create_folder(root)

    for key in obj:
        if type(obj[key]) is str:
            create_file(os.path.join(root, key), obj[key])
        if type(obj[key]) == dict:
            create_structure(os.path.join(root, key), obj[key])


def main(root, path_json):
    obj = json.loads(get_json_text(path_json))
    create_structure(root, obj)


if __name__ == '__main__':
    try:
        main("./output", "./input/source2.json")
    except Exception as e:
        print(e)
        