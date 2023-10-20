from django.shortcuts import render

def producto(request):
    productos = {"nombre1":"Electronica","nombre2":"Juguetes","nombre3":"Ropa"}
    return render(request, 'ejercicioProductos/index.html', productos)

def detalles(request):
    producto_uno = {"general":"Electronica",
                    "imagen1":"../static/images/mac.png",
                    "imagen2":"../static/images/Iphone.png",
                    "imagen3":"../static/images/playstation.png",
                    "nombre1":"Mac",
                    "nombre2":"iPhone",
                    "nombre3":"Playstation"}
    return render(request, 'ejercicioProductos/productos.html',producto_uno)

def detalles2(request):
    producto_dos = {"general":"Juguetes",
                    "imagen1":"../static/images/auto.png",
                    "imagen2":"../static/images/pelota.png",
                    "imagen3":"../static/images/figura.png",
                    "nombre1":"Auto",
                    "nombre2":"Pelota de Futbol",
                    "nombre3":"Figura de Accion"}
    return render(request, 'ejercicioProductos/productos.html',producto_dos)

def detalles3(request):
    producto_tres = {"general":"Ropa",
                     "imagen1":"../static/images/pantalon.png",
                     "imagen2":"../static/images/chaqueta.png",
                     "imagen3":"../static/images/camisa.png",
                     "nombre1":"Pantalon",
                     "nombre2":"Chaqueta",
                     "nombre3":"Camisa"}
    return render(request, 'ejercicioProductos/productos.html',producto_tres)
