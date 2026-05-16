"""
Script orquestador - Prueba 2: Scenario Outline con 30 casuísticas.
Compara velocidad entre Playwright y Selenium ejecutando múltiples iteraciones.

Uso:
    python run_comparativa_masivo.py
"""

import subprocess
import time
import sys
import os


def run_behave(project_dir, label, feature_file):
    """Ejecuta behave con un feature específico y mide el tiempo."""
    print(f"\n{'='*60}")
    print(f"  Ejecutando: {label}")
    print(f"  Feature: {feature_file}")
    print(f"  Casuísticas: 30")
    print(f"{'='*60}")

    start = time.time()
    result = subprocess.run(
        [sys.executable, "-m", "behave", "--no-capture", f"features/{feature_file}"],
        cwd=project_dir,
        capture_output=True,
        text=True,
    )
    elapsed = time.time() - start

    # Mostrar solo resumen, no todo el output
    lines = result.stdout.strip().split("\n")
    for line in lines[-5:]:
        print(f"  {line}")
    if result.returncode != 0 and result.stderr:
        print(f"  STDERR: {result.stderr[:200]}")

    return elapsed, result.returncode


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    selenium_dir = os.path.join(base_dir, "Selenium")
    playwright_dir = os.path.join(base_dir, "Playwright")

    feature = "login_masivo.feature"

    print("\n" + "=" * 60)
    print("  COMPARATIVA #2: SCENARIO OUTLINE (30 casuísticas)")
    print("  PLAYWRIGHT vs SELENIUM con Behave")
    print("=" * 60)

    # Ejecutar Selenium
    selenium_time, selenium_rc = run_behave(selenium_dir, "SELENIUM", feature)

    # Ejecutar Playwright
    playwright_time, playwright_rc = run_behave(playwright_dir, "PLAYWRIGHT", feature)

    # Resultados
    print("\n" + "=" * 60)
    print("  RESULTADOS - PRUEBA MASIVA (30 iteraciones)")
    print("=" * 60)
    print(f"  Selenium  : {selenium_time:.3f}s {'✓' if selenium_rc == 0 else '✗ (falló)'}")
    print(f"  Playwright: {playwright_time:.3f}s {'✓' if playwright_rc == 0 else '✗ (falló)'}")
    print(f"  {'─'*56}")

    if selenium_time > 0 and playwright_time > 0:
        # Tiempo por iteración
        print(f"  Selenium   por caso: {(selenium_time/30)*1000:.0f}ms")
        print(f"  Playwright por caso: {(playwright_time/30)*1000:.0f}ms")
        print(f"  {'─'*56}")

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
