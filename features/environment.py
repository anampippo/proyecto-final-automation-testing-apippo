# features/environment.py

import os
import datetime
from selenium import webdriver
from utils.logger import logger

# Carpeta para screenshots
SCREENSHOT_DIR = os.path.join(os.getcwd(), "reports", "screens")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def before_all(context):
    """Se ejecuta una vez antes de toda la suite"""
    logger.info("Inicializando WebDriver para toda la suite BDD")
    # Configuración básica de Chrome, podes agregar más opciones
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)

def after_step(context, step):
    """Se ejecuta después de cada step"""
    if step.status == "failed":
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        feature_name = context.feature.name.replace(" ", "_")
        scenario_name = context.scenario.name.replace(" ", "_")
        filename = f"{feature_name}__{scenario_name}__{timestamp}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        logger.info(f"Step fallido: '{step.name}'. Guardando screenshot en {filepath}")
        try:
            context.driver.save_screenshot(filepath)
        except Exception as e:
            logger.error(f"No se pudo guardar screenshot: {e}")

def after_all(context):
    """Se ejecuta una vez al finalizar toda la suite"""
    logger.info("Finalizando WebDriver y cerrando recursos")
    try:
        context.driver.quit()
    except Exception as e:
        logger.error(f"Error cerrando WebDriver: {e}")
