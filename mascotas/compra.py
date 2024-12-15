class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, articulo):
        if articulo.codigo not in self.carrito.keys():
            self.carrito[articulo.codigo]={
                "codigo": articulo.codigo, 
                "nombre": articulo.nombre,
                "precio": str (articulo.precio),
                "cantidad": 1,
                "total": articulo.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==articulo.codigo:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = articulo.precio
                    value["total"]= (value["total"]) + (articulo.precio)
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, articulo):
        id = articulo.codigo
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,articulo):
        for key, value in self.carrito.items():
            if key == articulo.codigo:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- (int(articulo.precio))
                if value["cantidad"] < 1:   
                    self.eliminar(articulo)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 