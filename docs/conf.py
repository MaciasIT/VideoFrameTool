import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'VideoFrameTool'
copyright = '2025, Michel Macias IT'
author = 'Michel Macias IT'
release = 'https://github.com/MaciasIT/VideoFrameTool'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',  # Esta es opcional pero muy útil
    'sphinx.ext.autosummary',  # ¡Añade esta línea!
    'sphinx.ext.napoleon',  # Si usas docstrings estilo Google o NumPy
    'sphinx.ext.intersphinx',  # Para enlazar con la documentación de otras librerías
    'sphinx.ext.todo',  # Si quieres incluir tareas pendientes en la documentación
    'myst_parser',

]

autosummary_generate = True
autosummary_patterns = ['api/*.rst']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'VideoFrameTool'
language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
