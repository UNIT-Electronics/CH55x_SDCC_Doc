
project = 'Cocket Nova Development Board Programming Guide C/C++'
copyright = '2024, Unit Electronics'
author = 'Cesar Bautista'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinx_togglebutton',
    'rst2pdf.pdfbuilder',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',  # Add this extension


]


templates_path = ['_templates']
html_theme_options = {
    "theme_switcher": False,  # Desactiva el interruptor de cambio de tema
}
exclude_patterns = []
master_doc = 'index'
numfig = True

html_theme = 'sphinx_book_theme'
html_logo = "_static/Logo-UNIT_Web-04-800x182.png"
html_static_path = ['_static']
latex_logo = "_static/Logo-UNIT_Web-04-800x182.png"

html_css_files = [
    'custom.css',
]