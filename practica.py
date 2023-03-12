class Producto():
    def __init__(self,nombre,unidades,precio):
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio
    def total(self):
        print(f'Total:{self.unidades*self.precio}€')

producto1=Producto('camisa',1555,9.95)
producto2=Producto('chaquetas',20,19.95)

producto1.total()
producto2.total()
