"""
run_tests.py

Ejecuta todos los tests del proyecto automáticamente.
"""

import unittest

if __name__ == "__main__":
    print("🔍 Ejecutando todos los tests del proyecto...\n")
    loader = unittest.TestLoader()
    suite = loader.discover("tests")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\n✅ Todos los tests pasaron correctamente.")
    else:
        print("\n❌ Algunos tests fallaron.")