import inspect
from Classes.animal import Animal

def get_animals_types():
    animal_classes = [cls for cls in inspect.getmembers(globals(), inspect.isclass)
                      if issubclass(cls[1], Animal)]
    return animal_classes


def display_animal_type_choices():
    animal_types = get_animals_types()
    index = 1
    for type in animal_types:
        print(f"{index}. {type}")
        index += 1