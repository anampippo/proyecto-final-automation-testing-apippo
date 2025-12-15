# Proyecto Final – Automation Testing QA

## 📌 Propósito del Proyecto

Este proyecto corresponde al **Trabajo Final Integrador** del curso de **Automation Testing QA**.
El objetivo es desarrollar un **framework de automatización de pruebas completo en Python**, aplicando buenas prácticas de diseño, automatización de pruebas de **UI y API**, y generación de reportes.

El framework fue diseñado para ser **escalable, mantenible y fácil de extender**, permitiendo la incorporación de nuevos casos de prueba tanto de interfaz como de servicios.

---

## 🛠️ Tecnologías Utilizadas

* Python 3
* Pytest
* Selenium WebDriver
* Requests
* Page Object Model (POM)
* Pytest HTML Report
* Logging
* Git & GitHub

---

## 📁 Estructura del Proyecto

```
proyecto-final-automation-testing-apippo/
│
├── pages/                 # Page Objects de UI
├── tests/                 # Tests de UI y API (Pytest)
├── features/              # Features y Steps para BDD (Behave)
│   ├── dummy.feature
│   ├── login.feature
│   ├── cart.feature
│   └── steps/
│       ├── dummy_steps.py
│       ├── login_steps.py
│       └── cart_steps.py
├── reports/               # Reportes HTML y JSON generados
│   └── screens/           # Screenshots de fallos
├── utils/                 # Utilidades comunes
├── pytest.ini             # Configuración de pytest
├── behave.ini             # Configuración de Behave
├── requirements.txt       # Dependencias
└── README.md
```

## 🧪 Tipos de Pruebas Implementadas

### 🔹 Pruebas de UI (Selenium)

* Login exitoso
* Login con credenciales inválidas (escenario negativo)
* Flujo completo de compra (login → selección de producto → checkout)
* Implementación del patrón **Page Object Model**
* Separación de lógica de test y lógica de página

### 🔹 Pruebas de API (Requests)

* GET /users
* POST /users
* DELETE /users/{id}

⚠️ **Nota:**
Los tests de API están marcados como `xfail` debido a restricciones del endpoint público **ReqRes**, el cual devuelve código **403** para requests automatizados.
Los flujos, validaciones y aserciones están correctamente implementados y la limitación externa se documenta sin afectar la ejecución del framework.

---

## 🧩 BDD (Behave)

### Features

* `login.feature`: Login exitoso + 3 escenarios de error (usuario bloqueado, contraseña incorrecta, campos vacíos)
* `cart.feature`: Agregar producto "Sauce Labs Backpack" con Background de login
* `dummy.feature`: Ejemplo de feature dummy para pruebas iniciales

### Steps

* `login_steps.py` y `cart_steps.py`: Conectan los steps con **Page Objects** y logging
* Steps implementan métodos de `LoginPage` e `InventoryPage` con logs informativos

### Hooks (`environment.py`)

* `before_all()`: Inicializa WebDriver
* `after_step()`: Captura screenshots automáticos en fallos en `reports/screens/`
* `after_all()`: Cierra WebDriver

---

## ⚙️ Instalación del Proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/proyecto-final-automation-testing-apippo.git
cd proyecto-final-automation-testing-apippo
```

2. Crear y activar un entorno virtual (opcional):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución de las Pruebas

### Behave

```bash
python3 -m behave --dry-run      # Verifica que Behave reconoce los features
python3 -m behave -t @smoke     # Ejecuta solo smoke tests
```

### Pytest

```bash
pytest tests_behave/ -v         # Ejecuta la suite BDD desde Pytest
pytest --html=reports/report.html --self-contained-html  # Genera reporte HTML
```

### Reportes

* Carpeta `reports/` con reportes HTML y JSON
* Carpeta `reports/screens/` con screenshots de fallos
* Información de cada test: Passed / XFailed, duración, evidencia

---

## 🚀 Consideraciones Finales

* Las pruebas son independientes entre sí
* El framework es fácilmente escalable
* La estructura facilita el mantenimiento y la incorporación de nuevos tests
* Los archivos BDD permiten comunicación clara con stakeholders no técnicos
* Preparación para integración CI/CD

Autor: Anabella Pippo
Proyecto Final – Automation Testing QA
