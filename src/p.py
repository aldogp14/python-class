from re import S


class animal():
    # atributos de la clase
    vivo = True

    # atributos de la instancia
    nombre = ""
    alimentacion = ""
    edad = 0
    progenie = 0
    # metodos

    def __init__(self, nombre, alimentacion, edad, progenie):
        self.nombre = nombre
        self.alimentacion = alimentacion
        self.edad = edad
        self.progenie = progenie

    def haz_ruido(self):
        print("waaaaaaa")


tortuga = animal("tortuga", "charales", 4, 2)


class perro(animal):
    # atributos de la clase
    amigable = True

    # metodo (overriding)
    def haz_ruido(self):
        print("guau")


class gato(animal):
    # atributos de la clase
    usa_arenero = False

    # metodo (overriding)
    def haz_ruido(self):
        print("miau")


snoopy = perro("snoopy", "croquetas", 7, 14)

manchas = gato("manchas", "croquetas", 3, 1)

print(f"{tortuga.__dict__}\n{snoopy.__dict__}\n{manchas.__dict__}\n")

print(snoopy.haz_ruido(), manchas.haz_ruido())
