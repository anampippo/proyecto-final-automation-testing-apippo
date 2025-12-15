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
* Behave (BDD)
* Page Object Model (POM)
* Pytest HTML Report
* Logging
* Git & GitHub

---

## 📁 Estructura del Proyecto

proyecto-final-automation-testing-apippo/
│
├── pages/              # Page Objects de UI
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
│
├── tests/              # Tests de UI y API (Pytest)
│   ├── api/
│   │   └── test_reqres_api.py
│   └── ui/
│       ├── test_login.py
│       ├── test_purchase_flow.py
│       └── users.json
│
├── features/           # Features y Steps para BDD (Behave)
│   ├── dummy.feature
│   └── steps/
│       └── dummy_steps.py
│
├── reports/            # Reportes HTML y JSON generados
│   └── report.html
│
├── utils/              # Utilidades comunes
│   ├── driver_factory.py
│   └── logger.py
│
├── pytest.ini          # Configuración de pytest
├── behave.ini          # Configuración de Behave (si existe)
├── requirements.txt    # Dependencias
└── README.md           # Documentación del proyecto


---

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
Los tests de API están marcados como `xfail` debido a restricciones del endpoint público **ReqRes**, que devuelve código **403** para requests automatizados.
Los flujos, validaciones y aserciones están correctamente implementados y la limitación externa se documenta sin afectar la ejecución del framework.

### 🔹 Pruebas BDD (Behave)

* Features configuradas: `dummy.feature`
* Scenarios: `@smoke` y `@regression`
* Todos los pasos (`steps`) implementados y ejecutables
* Reportes generados: `reports/behave.json` (JSON) y consola
* Validación exitosa de la ejecución (`--dry-run` y ejecución normal)

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

### Pytest (UI y API)

* Ejecutar todas las pruebas:

```bash
python3 -m pytest
```

* Ejecutar pruebas generando reporte HTML:

```bash
python3 -m pytest --html=reports/report.html --self-contained-html
```

### Behave (BDD)

* Verificar que Behave reconoce los features:

```bash
python3 -m behave --dry-run
```

* Ejecutar solo smoke tests:

```bash
python3 -m behave -t @smoke
```

* Ejecutar solo regression tests:

```bash
python3 -m behave -t @regression
```

* Generar reporte JSON:

```bash
python3 -m behave -f json -o reports/behave.json -f pretty
```

---

## 📊 Reportes

* Los reportes de Pytest se guardan en `reports/report.html`
* Los reportes de Behave se guardan en `reports/behave.json`
* Incluyen:

  * Estado de los tests (Passed / XFailed)
  * Duración de ejecución
  * Evidencia clara del resultado de cada prueba

---

## 🚀 Consideraciones Finales

* Las pruebas son independientes entre sí
* El framework es fácilmente escalable
* La estructura facilita el mantenimiento y la incorporación de nuevos tests
* El proyecto cumple con todos los requisitos solicitados en la consigna

---

**Autor:** Anabella Pippo
**Proyecto Final – Automation Testing QA**
