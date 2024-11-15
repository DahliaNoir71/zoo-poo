from Classes.zoo import Zoo
from services.zoo_service import display_animal_type_choices

zootopia = Zoo("Zootopia")

while True:
        print("\nWelcome to the Zootopia!")
        print("1. Add an animal")
        # print("2. Remove an animal")
        # print("3. Display animals")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_animal_type_choices()
            animal_type = input("Enter the type of animal: ")
            if animal_type:
                animal_name = input("Enter the name of the animal: ")
                if animal_name:
                    new_animal = eval(animal_type)(animal_name)
                    zootopia.add_animal(new_animal)
                    print(zootopia)
                else:
                    print("Please enter a valid name.")

        # elif choice == "2":
        #     animal = input("Enter the name of the animal: ")
        #     zootopia.remove_animal(animal)
        #     print(f"{animal} has been removed from the zoo.")
        # elif choice == "3":
        #     zootopia.display_animals()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")