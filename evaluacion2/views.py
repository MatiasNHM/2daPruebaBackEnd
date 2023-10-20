from django.shortcuts import render

def vistaGeneral(request):

    datos = {
              "nombre":"Tipos De Cubos Rubik's",
              "descripcion":"Se observara precios sobre 4 tipos de cubos rubik's y como las estrellas de valoracion",
              "descripcion2":"Si desea observar cubos precione uno de los botones",
              "descripcion3":"Y asi revisar lo que el titulo dice",
              "descripcion3":"Informacion sobre los cubos",
              "img":"../static/images/rubik3x3.png",
              "opcion1":"Cubo Rubik 1 x 1",
              "opcion2":"Cubo Rubik 2 x 2",
              "opcion3":"Cubo Rubik 3 x 3",
              "ir1":"../rubik1",
              "ir2":"../rubik2",
              "ir3":"../rubik3",
              "opcion4":"Ir a productos",
              "ir4":"../productos"
             }

    return render(request, 'evaluacion2/index.html',datos)

def vista1(request):

    datos1 = {
              "nombre":"Cubo Rubik 1 x 1",
              "descripcion":"""El Cubo de Rubik 1x1 es un bloque cúbico con 6 sticker de colores que simulan un cubo de rubik. 
                               Ahora podrás completar tu colección de cubos cúbicos con este completo Cubo de Rubik 1x1.""",
              "descripcion2":"Ahora podrás completar tu colección de cubos cúbicos con este completo Cubo de Rubik 1x1.",
              "precio":"$7.000-$12.000 (los de calidad aceptable)",
              "valorado":"★★★☆☆",
              "img":"../static/images/rubik1x1.png",
              "opcion1":"Cubo Rubik 2 x 2",
              "opcion2":"Cubo Rubik 3 x 3",
              "opcion3":"Cubo Rubik 4 x 4",
              "opcion4":"Volver",
              "ir1":"../rubik2",
              "ir2":"../rubik3",
              "ir3":"../rubik3",
              "ir4":"../"
             }

    return render(request, 'evaluacion2/index.html',datos1)

def vista2(request):

    datos2 = {
              "nombre":"Cubo Rubik 2 x 2",
              "descripcion":"""Los cubos 2x2 son los más pequeños dentro de los modelos cúbicos y los que más rápido se resuelven. 
                               Tienen un tamaño estándar de 50mm y un peso aproximado de 70 gr. """,
              "descripcion2":"¡Los mejores del mundo pueden llegar a resolverlo en medio segundo!",
              "precio":"$5.000-$9.000 (los de calidad aceptable)",
              "valorado":"★★★★☆",
              "img":"../static/images/rubik2x2.png",
              "opcion1":"Cubo Rubik 1 x 1",
              "opcion2":"Cubo Rubik 3 x 3",
              "opcion3":"Cubo Rubik 4 x 4",
              "opcion4":"Volver",
              "ir1":"../rubik1",
              "ir2":"../rubik3",
              "ir3":"../rubik4",
              "ir4":"../"
             }

    return render(request, 'evaluacion2/index.html',datos2)

def vista3(request):

    datos3 = {
              "nombre":"Cubo Rubik 3 x 3",
              "descripcion":"Un cubo de Rubik de 3x3 tiene seis caras, cada una de un color diferente.",
              "descripcion2": """El centro de cada cara está unido a la estructura central, eje que mantiene unido el cubo, 
                               por lo que no se mueven más allá de girar cuando se mueve toda esa cara.""",
              "precio":"$8.000-$13.000 (los de calidad aceptable)",
              "valorado":"★★★★★",
              "img":"../static/images/rubik3x3.png",
              "opcion1":"Cubo Rubik 1 x 1",
              "opcion2":"Cubo Rubik 2 x 2",
              "opcion3":"Cubo Rubik 4 x 4",
              "opcion4":"Volver",
              "ir1":"../rubik1",
              "ir2":"../rubik2",
              "ir3":"../rubik4",
              "ir4":"../"
             }

    return render(request, 'evaluacion2/index.html',datos3)

def vista4(request):

    datos4 = {
              "nombre":"Cubo Rubik 4 x 4",
              "descripcion":"""El 4x4 está formado por ocho esquinas, veinticuatro piezas centrales que 
                               forman los seis centros y otras veinticuatro piezas que forman las doce aristas.""",
              "descripcion2":"Y de aqui empieza como los otros cubos en el cual mientras mayor cantidad, mas dificil no es, si no que es mas largo resolverlo",
              "precio":"$15.000-$20.000 (los de calidad aceptable)",
              "valorado":"★★★★☆",
              "img":"../static/images/rubik4x4.png",
              "opcion1":"Cubo Rubik 1 x 1",
              "opcion2":"Cubo Rubik 2 x 2",
              "opcion3":"Cubo Rubik 3 x 3",
              "opcion4":"Volver",
              "ir1":"../rubik1",
              "ir2":"../rubik2",
              "ir3":"../rubik3",
              "ir4":"../"
             }

    return render(request, 'evaluacion2/index.html',datos4)


