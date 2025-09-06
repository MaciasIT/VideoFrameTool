import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import tempfile
import zipfile
from zipper import zip_folder

class TestZipper(unittest.TestCase):

    def test_zip_folder(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Crear archivos simulados
            file1 = os.path.join(tmpdir, "img1.png")
            file2 = os.path.join(tmpdir, "img2.png")
            with open(file1, "w") as f:
                f.write("test image 1")
            with open(file2, "w") as f:
                f.write("test image 2")

            # Comprimir carpeta
            zip_path = zip_folder(tmpdir)
            self.assertTrue(os.path.isfile(zip_path))

            # Verificar contenido del zip
            with zipfile.ZipFile(zip_path, "r") as zipf:
                contents = zipf.namelist()
                self.assertIn("img1.png", contents)
                self.assertIn("img2.png", contents)