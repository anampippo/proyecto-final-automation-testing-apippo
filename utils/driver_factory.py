from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    service = Service(ChromeDriverManager().install())  # Crea la instancia del servicio
    driver = webdriver.Chrome(service=service)  # Usá la instancia en lugar de instalar directo
    driver.maximize_window()  # Maximiza la ventana
    return driver
