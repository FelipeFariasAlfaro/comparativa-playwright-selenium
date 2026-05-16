# Comparativa de Velocidad: Playwright vs Selenium

## Objetivo

Medir y comparar el rendimiento de **Playwright** y **Selenium** ejecutando flujos idénticos de automatización web con **Behave** (BDD) como framework de pruebas.

---

## Entorno de Pruebas

| Aspecto | Detalle |
|---------|---------|
| Sistema Operativo | Windows |
| Navegador | Chromium (headless) |
| Framework BDD | Behave 1.3.3 |
| Selenium | 4.43.0 |
| Playwright | 1.52.0 |
| Sitio objetivo | https://the-internet.herokuapp.com/login |
| Python | 3.14 |

---

## Pruebas Ejecutadas

| Prueba | Script | Escenarios | Descripción |
|--------|--------|------------|-------------|
| #1 - Básica | `run_comparativa.py` | 2 | Login exitoso + login fallido |
| #2 - Masiva | `run_comparativa_masivo.py` | 30 | Scenario Outline con 30 combinaciones de credenciales |

---

## Tabla Comparativa de Arquitectura

| Característica | Selenium | Playwright |
|----------------|----------|------------|
| Protocolo de comunicación | WebDriver (HTTP JSON Wire) | CDP (Chrome DevTools Protocol) directo |
| Gestión del navegador | ChromeDriver externo | Bundled, sin proceso intermedio |
| Espera de navegación | Manual (explicit/implicit waits) | Automática (auto-wait) |
| Modelo de ejecución | Comandos síncronos vía HTTP | Comunicación directa por WebSocket |
| Overhead por comando | Alto (HTTP request/response por cada acción) | Bajo (mensajes binarios por socket) |
| Arranque del navegador | Requiere descargar/configurar driver | `playwright install` gestiona todo |
| Aislamiento de contexto | Cookies/sesión compartida por defecto | Cada `new_page()` es contexto limpio |
| Manejo de páginas nuevas | Esperar staleness + buscar elemento | Espera automática post-navegación |

---

## Por Qué Playwright es Más Rápido

| Factor | Impacto |
|--------|---------|
| **Sin intermediario HTTP** | Selenium envía cada comando como un request HTTP al ChromeDriver, que lo traduce a CDP. Playwright habla CDP directamente. Esto elimina la latencia de serialización/deserialización JSON y el overhead TCP por cada acción. |
| **Auto-wait inteligente** | Playwright espera automáticamente a que los elementos sean accionables antes de interactuar. Selenium requiere waits explícitos que añaden polling y tiempo muerto. |
| **Conexión persistente** | Playwright mantiene un WebSocket abierto con el navegador. Selenium abre y cierra conexiones HTTP por cada comando. |
| **Menos procesos** | Selenium necesita: Python → ChromeDriver → Chrome. Playwright necesita: Python → Chrome. Un salto menos en la cadena. |
| **Navegación optimizada** | Playwright detecta automáticamente cuándo una navegación termina. En Selenium hay que implementar patrones como `staleness_of` manualmente, añadiendo complejidad y tiempo. |

---

## Estructura del Proyecto

```
Comparativa/
├── run_comparativa.py            # Prueba #1: 2 escenarios
├── run_comparativa_masivo.py     # Prueba #2: 30 escenarios
├── COMPARATIVA.md                # Este documento
├── README.md                     # Instrucciones de uso
├── Playwright/
│   ├── requirements.txt
│   └── features/
│       ├── environment.py
│       ├── login.feature
│       ├── login_masivo.feature
│       └── steps/
│           └── login_steps.py
└── Selenium/
    ├── requirements.txt
    └── features/
        ├── environment.py
        ├── login.feature
        ├── login_masivo.feature
        └── steps/
            └── login_steps.py
```

---

## Resultados

> Completar después de ejecutar las pruebas.

### Prueba #1 - Básica (2 escenarios)

| Framework | Tiempo | Estado |
|-----------|--------|--------|
| Selenium | ___ s | ⬜ |
| Playwright | ___ s | ⬜ |

### Prueba #2 - Masiva (30 escenarios)

| Framework | Tiempo total | Tiempo por caso | Estado |
|-----------|-------------|-----------------|--------|
| Selenium | ___ s | ___ ms | ⬜ |
| Playwright | 77.7 s | ~2593 ms | ✅ |

---

## Conclusiones

| Aspecto | Ganador | Nota |
|---------|---------|------|
| Velocidad de ejecución | Playwright | Menos overhead por comando |
| Facilidad de setup | Playwright | No requiere driver externo |
| Manejo de waits | Playwright | Auto-wait vs explicit waits manuales |
| Ecosistema/comunidad | Selenium | Más maduro, más documentación legacy |
| Soporte multi-navegador | Empate | Ambos soportan Chrome, Firefox, Edge |
| Compatibilidad con Behave | Empate | Ambos se integran sin problemas |

---

## Cómo Ejecutar

```bash
# Instalar dependencias
pip install -r Selenium/requirements.txt
pip install -r Playwright/requirements.txt
playwright install chromium

# Prueba básica
python run_comparativa.py

# Prueba masiva (30 escenarios)
python run_comparativa_masivo.py
```
