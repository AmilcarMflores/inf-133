# Recibe una lista de animales y formatea 
def render_animal_list(animals):
    # Representa una lista de animales como una lista de diccionarios
    return [
        {
            "id": animal.id,
            "name": animal.name,
            "species": animal.species,
            "age": animal.age,
        }
        # for de comprensión itera una lista al elemento 
        for animal in animals
    ]

# un animal
def render_animal_detail(animal):
    # Representa los detalles de un animal como un diccionario
    return {
        "id": animal.id,
        "name": animal.name,
        "species": animal.species,
        "age": animal.age,
    }
    