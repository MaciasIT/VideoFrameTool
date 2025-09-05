# docs/conf.py
import os
import sys
from datetime import date

# Inserta la carpeta raíz del repo en el path para que autodoc pueda importar los módulos
sys.path.insert(0, os.path.abspath('..'))

project = 'VideoFrameTool'
author = 'Tu Nombre'
release = '0.1.0'
year = date.today().year

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',   # docstrings estilo Google/NumPy
    'sphinx.ext.viewcode',   # enlaces "ver código"
    'sphinx.ext.todo',
    'myst_parser',           # permite .md
    'sphinx_copybutton',     # botón para copiar código
]

# Generar automáticamente páginas de autosummary
autosummary_generate = True

# Autodoc: orden y miembros
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

# Napoleon (docstrings estilo Google)
napoleon_google_docstring = True
napoleon_numpy_docstring = False

templates_path = ['_templates']
exclude_patterns = []

# Tema
html_theme = 'furo'   # moderno; alternativa: 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = f'{project} {release}'
html_last_updated_fmt = '%Y-%m-%d'
