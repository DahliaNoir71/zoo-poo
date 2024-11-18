import inspect
from Classes.animal import Animal

def get_animals_types():
    subclasses = []
    for module in inspect.getmembers(inspect.getmodule(Animal), inspect.ismodule):
        if module[1] is not None:
            for cls in inspect.getmembers(module[1], inspect.isclass):
                if issubclass(cls[1], Animal) and cls[1] is not Animal:
                    subclasses.append(cls)
    return subclasses


def display_animal_type_choices():
    animal_types = get_animals_types()
    index = 1
    for type in animal_types:
        print(f"{index}. {type}")
        index += 1