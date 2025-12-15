from behave import given, when, then
from pages.login_page import LoginPage   # ahora sí apunta a la carpeta pages/
from utils.logger import logger           # apunta a la carpeta utils/
from behave.api.pending_step import StepNotImplementedError


@given(u'el usuario está logueado y en la página de inventario')
def step_impl(context):
    # Asume que ya hiciste login en el Background
    context.inventory_page = InventoryPage(context.driver)
    logger.info("Usuario logueado y en inventario")

@when(u'agrega "{producto}" al carrito')
def step_impl(context, producto):
    context.inventory_page.add_to_cart(producto)
    logger.info(f"Producto agregado al carrito: {producto}")

@then(u'el contador del carrito muestra "{cantidad}"')
def step_impl(context, cantidad):
    count = context.inventory_page.get_cart_count()
    assert str(count) == cantidad, f"El contador muestra {count}, esperado {cantidad}"
    logger.info(f"Contador del carrito correctamente actualizado a {cantidad}")