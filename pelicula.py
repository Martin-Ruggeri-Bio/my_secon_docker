class Pelicula():
    def __init__(self, codigo=0, nombre=''):
        self.codigo = codigo
        self.nombre = nombre

    def __srt__(self):
        return "nombre: %d %s" % (self.codigo, self.nombre)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        self._codigo = value


class Catalogo():
    def __init__(self):
        self.catalogo = {}

    @property
    def catalogo(self):
        return self._catalogo

    @catalogo.setter
    def catalogo(self, value):
        self._catalogo = value

    def __str__(self):
        string = ''
        for pelicula in self.catalogo.values():
            string += '\nNombre: ' + pelicula.nombre
        return string

    def add(self, pelicula):
        self.catalogo[pelicula.codigo] = pelicula


if __name__ == '__main__':
    pelicula = Pelicula(1, "Aves de Presa")
    catalogo = Catalogo()
    catalogo.add(pelicula)

    pelicula = Pelicula(2, "Mision Imposible")
    catalogo.add(pelicula)

    print(catalogo.__str__())
