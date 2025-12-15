from behave import given, when, then
from pages.login_page import LoginPage   # ahora sí apunta a la carpeta pages/
from utils.logger import logger           # apunta a la carpeta utils/
from behave.api.pending_step import StepNotImplementedError


@given(u'el usuario está en la página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    logger.info("Usuario abre la página de login")

@when(u'el usuario ingresa usuario "{usuario}" y contraseña "{password}"')
def step_impl(context, usuario, password):
    context.login_page.login(usuario, password)
    logger.info(f"Usuario intenta login con {usuario} / {password}")

@then(u'el usuario es redirigido al inventario')
def step_impl(context):
    assert context.login_page.is_logged_in(), "No se redirigió al inventario"
    logger.info("Usuario redirigido correctamente al inventario")

@then(u'se muestra un mensaje de error')
def step_impl(context):
    assert context.login_page.is_error_displayed(), "No se mostró mensaje de error"
    logger.info("Mensaje de error visible al usuario")
