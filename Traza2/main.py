from categoria import Categoria
from unidad_medida import Unidad_Medida
from articulo_insumo import Articulo_Insumo
from articulo_manufacturado import Articulo_Manufacturado
from articulo_manufacturado_detalle import Articulo_Manufacturado_Detalle
from imagen import Imagen

#CATEGORIAS
cat_pizza = Categoria(denominacion='Pizza',id=1)
cat_sandwich = Categoria(denominacion='Sandwich',id=1)
cat_insumos = Categoria(denominacion='Lomos',id=1)

#UNIDAD MEDIDAS
litros = Unidad_Medida(denominacion='Litro',id=1)
kilogramos = Unidad_Medida(denominacion='Kilogramos',id=1)
gramos = Unidad_Medida(denominacion='Gramos',id=1)

#ARTICULOS INSUMO
sal = Articulo_Insumo(precioCompra=100,stockActual=20,stockMaximo=40, es_para_elaborar=True, denominacion="sal")
aceite = Articulo_Insumo(precioCompra=500,stockActual=10,stockMaximo=55, es_para_elaborar=True, denominacion="aceite")
carne = Articulo_Insumo(precioCompra=10000,stockActual=20,stockMaximo=20, es_para_elaborar=True, denominacion="carne")
harina = Articulo_Insumo(precioCompra=10,stockActual=15,stockMaximo=40, es_para_elaborar=True, denominacion="harina")

#IMAGEN
hawaina_pizza1 = Imagen(denominacion='Pizza',id=1)
hawaina_pizza2 = Imagen(denominacion='Pizza',id=2)
hawaina_pizza3 = Imagen(denominacion='Pizza',id=3)
lomo_completo1 = Imagen(denominacion='Lomos',id=1)
lomo_completo2 = Imagen(denominacion='Lomos',id=2)
lomo_completo3 = Imagen(denominacion='Lomos',id=3)
img_pizzas = {hawaina_pizza1, hawaina_pizza2, hawaina_pizza3}
img_lomos = {lomo_completo1, lomo_completo2, lomo_completo3}

#DETALLE
detalle_pizza_hawaina1 = Articulo_Manufacturado_Detalle(id =1, cantidad=1, articulo_insumo=sal)
detalle_pizza_hawaina2 = Articulo_Manufacturado_Detalle(id =2, cantidad=2, articulo_insumo=harina)
detalle_pizza_hawaina3 = Articulo_Manufacturado_Detalle(id =3, cantidad=1, articulo_insumo=aceite)
detalle_pizza_lomo1 = Articulo_Manufacturado_Detalle(id =1, cantidad=1, articulo_insumo=sal)
detalle_pizza_lomo2 = Articulo_Manufacturado_Detalle(id =2, cantidad=1, articulo_insumo=aceite)
detalle_pizza_lomo3 = Articulo_Manufacturado_Detalle(id =3, cantidad=1, articulo_insumo=carne)
detalles_pizzas = {detalle_pizza_hawaina1, detalle_pizza_hawaina2, detalle_pizza_hawaina3}
detalles_lomos = {detalle_pizza_lomo1, detalle_pizza_lomo2, detalle_pizza_lomo3}

#ARTICULO MANUFACTURADO
pizza_hawaina = Articulo_Manufacturado(
    denominacion="Pizza Hawaina",
    precioVenta=12.0,
    descripcion="Pizza con piña y jamón",
    tiempoEstimadoMinutos=20,
    preparacion="Hornear por 20 minutos",
    categoria=cat_pizza,
    unidad_medida=kilogramos,
    imagen=img_pizzas,
    detalles=detalles_pizzas,
    id=1)

lomo_completo = Articulo_Manufacturado(
    denominacion="Lomos",
    precioVenta=12.0,
    descripcion="Lomo completo",
    tiempoEstimadoMinutos=40,
    preparacion="Hornear por 40 minutos",
    categoria=cat_sandwich,
    unidad_medida=kilogramos,
    imagen=img_lomos,
    detalles=detalles_lomos,
    id=2)

#PRINTS
#categorias
categorias = [cat_pizza, cat_sandwich, cat_insumos]
print("Categorías:")
for cat in categorias:
    print(f"- {cat.denominacion} (ID: {cat.id})")

#articulos insumo
insumos = [sal, aceite, carne, harina]
print("\nArtículos Insumos:")
for insumo in insumos:
    print(f"- {insumo.denominacion}, Precio Compra: {insumo.precioCompra}, Stock: {insumo.stockActual}/{insumo.stockMaximo}")

#articulos manufacturado
manufacturados = [pizza_hawaina, lomo_completo]
print("\nArtículos Manufacturados:")
for prod in manufacturados:
    print(f"- {prod.denominacion}, Precio Venta: {prod.precioVenta}, Tiempo Estimado: {prod.tiempoEstimadoMinutos} min")

#articulos manufacturado por ID
def buscar_manufacturado_por_id(lista, id_buscar):
    for prod in lista:
        if prod.id == id_buscar:
            return prod
    return None

buscado = buscar_manufacturado_por_id(manufacturados, 101)
if buscado:
    print(f"\nArtículo Manufacturado encontrado por ID 101: {buscado.denominacion}")
else:
    print("\nNo se encontró el artículo con ID 101")

#actualizar articulos manufacturado ID
id_actualizar = 101
nuevo_precio = 15.0
prod_actualizar = buscar_manufacturado_por_id(manufacturados, id_actualizar)
if prod_actualizar:
    prod_actualizar.precioVenta = nuevo_precio
    print(f"\nPrecio actualizado de {prod_actualizar.denominacion}: {prod_actualizar.precioVenta}")

#eliminar articulos manufacturado ID

id_eliminar = 102
manufacturados = [prod for prod in manufacturados if prod.id != id_eliminar]
print("\nArtículos Manufacturados después de eliminar ID 102:")
for prod in manufacturados:
    print(f"- {prod.denominacion}")