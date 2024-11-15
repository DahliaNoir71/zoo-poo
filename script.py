from Classes.animal import Lion, Gazelle
from Classes.cage import Cage
from Classes.zoo import Zoo

zootopia = Zoo("Zootopia")
print(zootopia)

zootopia.add_nb_cages(2)
print(zootopia)

new_cage = Cage()
zootopia.add_cage(new_cage)
print(zootopia)

first_cage = zootopia.cages[0]
lion_mufasa = Lion("Mufasa")
first_cage.add_animal(lion_mufasa)
print(zootopia)

first_cage.add_animal(lion_mufasa)
print(zootopia)

lion_leo = Lion("Léo")
first_cage.add_animal(lion_leo)
print(zootopia)

gazelle_azelle = Gazelle("Azelle")
first_cage.add_animal(gazelle_azelle)
print(zootopia)

second_cage = zootopia.cages[1]
other_gazelle = Gazelle("Gaz Aile")
second_cage.add_animals([gazelle_azelle, other_gazelle])
print(zootopia)

