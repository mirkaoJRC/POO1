#Autor: Mirko Ramirez
#Primer EJemplo

class Mascota():
    def __init__(self, tipo, nombre, edad, Genero_Del_animal, color, raza):
        self.tipo = tipo
        self.nombre = nombre
        self.edad = edad
        self.Genero_del_animal = Genero_Del_animal
        self.color = color
        self.raza = raza

    def correr(self):
        print("{} empieza corriendo".format(self.nombre))

    def comer(self):
        print("El {} Come comida....".format(self.tipo))

    def __str__(self):
        return "Llego noche, a dormir..."

mascota1 = Mascota("perro" ,"Amigo" , 10, "Macho", "negro", "Rockwailler")
mascota1.comer()
#segundo EJemplo
class Dueño():

    def __init__(self, nombre, apellido, edad, Genero, Ci, Ciudad, domicilio):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.Genero = Genero
        self.Ci = Ci
        self.Ciudad = Ciudad
        self.domicilio =domicilio

    def pasenado(self):
        print("Sacando a pasear")

    def LLevando_veterinario(self):
        print("dirigiendo a veterinario")

    def __str__(self):
        return "nombre: {}, apellido: {}, edad: {}, Genero: {}, Ci{}, ciudad {}, domicilio {}".format(self.nombre, self.apellido,self.edad, self.Genero,self.Ci, self.ciudad, self.domicilio)