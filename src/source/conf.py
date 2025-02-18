
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
   "repository_url": "https://github.com/UNIT-Electronics/CH55x_SDCC_Doc",
    "repository_branch": "main",  # Rama principal de tu repositorio
      "path_to_docs": "docs/",  # Ruta a la documentación dentro del repositorio
    "use_repository_button": True,  # Muestra un botón que enlaza al repositorio
    "use_issues_button": True,  # Muestra un botón que enlaza a la sección de issues
    "use_edit_page_button": True,  # Muestra un botón para editar la página actual

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