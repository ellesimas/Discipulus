# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
#Antes comentadas por default, as três linhas acima 'abertas'
#e a terceira linha teve o caminho de path alterado para o código fonte
#do sistema:
#sys.path.insert(0, os.path.abspath('<caminho/para/o/codigo/fonte'))
sys.path.insert(0, os.path.abspath('../../src/mockbrython/'))

# -- Project information -----------------------------------------------------

project = "Tutorial Discipulu's"
copyright = '2020, Emanuelle Simas'
author = 'Emanuelle Simas'

# The full version, including alpha/beta/rc tags
release = '20.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

#'sphinx.ext.autodoc': Inclui documentação de docstring
#'sphinx.ext.viewcode': Adiciiona link ao codigo-fonte destacado
#'sphinx.ext.githubpages': Vincula ao github

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'default'
#Você pode encontrar outros temas no site:
#<https://www.sphinx-doc.org/en/master/usage/theming.html>

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
#Especifica o mestre. Tentativa primeira de solução de erro no rdd
master_doc = 'index'