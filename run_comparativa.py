"""
Script orquestador para comparar velocidad entre Playwright y Selenium con Behave.

Uso:
    python run_comparativa.py

Requisitos previos:
    1. pip install -r Selenium/requirements.txt
    2. pip install -r Playwright/requirements.txt
    3. playwright install chromium
"""

import subprocess
import time
import sys
import os


def run_behave(project_dir, label, feature_file="features/login.feature"):
    """Ejecuta behave en el directorio indicado y mide el tiempo."""
    print(f"\n{'='*60}")
    print(f"  Ejecutando: {label}")
    print(f"{'='*60}")

    start = time.time()
    result = subprocess.run(
        [sys.executable, "-m", "behave", "--no-capture", feature_file],
        cwd=project_dir,
        capture_output=True,
        text=True,
    )
    elapsed = time.time() - start

    print(result.stdout)
    if result.stderr:
        print(result.stderr)

    return elapsed, result.returncode


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    selenium_dir = os.path.join(base_dir, "Selenium")
    playwright_dir = os.path.join(base_dir, "Playwright")

    print("\n" + "=" * 60)
    print("  COMPARATIVA DE VELOCIDAD: PLAYWRIGHT vs SELENIUM")
    print("  Framework BDD: Behave")
    print("=" * 60)

    # Ejecutar Selenium
    selenium_time, selenium_rc = run_behave(selenium_dir, "SELENIUM + Behave")

    # Ejecutar Playwright
    playwright_time, playwright_rc = run_behave(playwright_dir, "PLAYWRIGHT + Behave")

    # Resultados
    print("\n" + "=" * 60)
    print("  RESULTADOS DE LA COMPARATIVA")
    print("=" * 60)
    print(f"  Selenium  : {selenium_time:.3f}s {'✓' if selenium_rc == 0 else '✗ (falló)'}")
    print(f"  Playwright: {playwright_time:.3f}s {'✓' if playwright_rc == 0 else '✗ (falló)'}")
    print(f"  {'─'*56}")

    if selenium_time > 0 and playwright_time > 0:
        if playwright_time < selenium_time:
            diff = selenium_time - playwright_time
            pct = (diff / selenium_time) * 100
            print(f"  Playwright fue {pct:.1f}% más rápido ({diff:.3f}s menos)")
        elif selenium_time < playwright_time:
            diff = playwright_time - selenium_time
            pct = (diff / playwright_time) * 100
            print(f"  Selenium fue {pct:.1f}% más rápido ({diff:.3f}s menos)")
        else:
            print("  Ambos tardaron lo mismo")

    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
