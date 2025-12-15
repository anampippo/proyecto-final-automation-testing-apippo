from behave import when, then
from pages.inventory_page import InventoryPage
from utils.logger import logger

@when(u'el usuario agrega "{producto}" al carrito')
def step_impl(context, producto):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.add_product_to_cart(producto)
    logger.info(f"Producto agregado al carrito: {producto}")

@then(u'el contador del carrito muestra "{cantidad}"')
def step_impl(context, cantidad):
    actual = context.inventory_page.get_cart_count()
    assert actual == int(cantidad), f"Esperado {cantidad}, pero se mostró {actual}"
    logger.info(f"Contador del carrito actualizado correctamente: {actual}")
