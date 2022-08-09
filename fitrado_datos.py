#cuando la variable se colocoa en mayuscula se deja como una variable constante
#esto se realiza por buenas practicas
from concurrent.futures.thread import _worker


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def rum():
    all_python_dev = [worker["name"] for worker in DATA if worker ["language"]=="python"]
    all_platzi_worker= [worker["name"] for worker in DATA if worker ["organization"]=="platzi"]

    adults= list(filter(lambda worker: worker["age"] > 18 ,DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people=list(map(lambda worker: worker | {"old": worker["age"]>70}, DATA)) # el | solo sirve de la version 3.9 de python para unir dos diccionarios con la sentencia q esta en el ejemplo.

    for worker in all_python_dev:
        print(worker)

    for worker in all_platzi_worker:
        print(worker)

    for worker in adults:
        print(worker)

    for worker in old_people:
        print(worker)
        








if __name__ =='__main__':
    rum()
#

