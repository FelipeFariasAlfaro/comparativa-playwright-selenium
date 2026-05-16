# Comparativa de Velocidad: Playwright vs Selenium

Proyecto para comparar la velocidad de ejecución de pruebas automatizadas usando **Behave** (BDD) con dos frameworks de automatización de navegador.

## Estructura

```
Comparativa/
├── run_comparativa.py          # Script orquestador
├── README.md
├── Playwright/
│   ├── requirements.txt        # playwright==1.52.0, behave==1.2.6
│   └── features/
│       ├── environment.py      # Setup/teardown de Playwright
│       ├── login.feature       # Escenarios BDD
│       └── steps/
│           └── login_steps.py  # Implementación de steps
└── Selenium/
    ├── requirements.txt        # selenium==4.33.0, behave==1.2.6
    └── features/
        ├── environment.py      # Setup/teardown de Selenium
        ├── login.feature       # Escenarios BDD (idéntico)
        └── steps/
            └── login_steps.py  # Implementación de steps
```

## Versiones

| Librería   | Versión |
|------------|---------|
| Selenium   | 4.43.0  |
| Playwright | 1.52.0  |
| Behave     | 1.3.3   |

## Instalación

```bash
# Crear entorno virtual (recomendado)
python -m venv venv
venv\Scripts\activate  # Windows

# Instalar dependencias de Selenium
pip install -r Selenium/requirements.txt

# Instalar dependencias de Playwright
pip install -r Playwright/requirements.txt
playwright install chromium
```

## Ejecución

### Comparativa completa (ambos frameworks)

```bash
python run_comparativa.py
```

### Ejecutar solo Selenium

```bash
cd Selenium
behave
```

### Ejecutar solo Playwright

```bash
cd Playwright
behave
```

## Flujo de prueba

Ambos proyectos ejecutan el mismo flujo contra [the-internet.herokuapp.com](https://the-internet.herokuapp.com/login):

1. Abrir la página de login
2. Ingresar credenciales (válidas e inválidas)
3. Hacer clic en el botón de login
4. Verificar el mensaje de resultado

## Notas

- Ambos navegadores se ejecutan en modo **headless** para una comparación justa.
- Se usa **Chrome/Chromium** en ambos casos.
- El tiempo medido incluye: apertura del navegador, navegación, interacción y cierre.
