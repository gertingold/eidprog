# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Einführung in das Programmieren für Physiker und Materialwissenschaftler'
copyright = '2010-2019, Gert-Ludwig Ingold, Lizenz: CC BY 4.0 International'
author = 'Gert-Ludwig Ingold'

# The full version, including alpha/beta/rc tags
release = '2019alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.doctest',
              'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'de'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

master_doc = 'index_latex'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'haiku'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = 'Einführung in das Programmieren für Physiker und Materialwissenschaftler'
html_short_title = 'Einführung in das Programmieren'
html_use_index = False
htmlhelp_basename = 'eidprogdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_documents = [
  ('index_latex', 'eidprog.tex',
   'Einführung in das Programmieren für Physiker und Materialwissenschaftler',
   'Gert-Ludwig Ingold', 'manual'),

]

latex_elements = {
        # The paper size ('letterpaper' or 'a4paper').
        'papersize': 'a4paper',
    
        # The font size ('10pt', '11pt' or '12pt').
        'pointsize': '10pt',
    
        # Additional stuff for the LaTeX preamble.
        'preamble': r'''
        \hypersetup{pdftitle={%s},
                    pdfauthor={Gert-Ludwig Ingold <gert.ingold@physik.uni-augsburg.de>},
                    pdfsubject={Manuskript zur Vorlesung »%s«},
                    pdfkeywords={Programmieren, Python, Vorlesungsmanuskript, PHM-0041, PHM-0042}}
        ''' % (latex_documents[0][2], latex_documents[0][2]),

        'printindex': '',
    
        # Latex figure (float) alignment
        #
        'figure_align': 'tbp',
    
        'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
        'sphinxsetup': '''verbatimwithframe=false,
                          VerbatimColor={named}{AliceBlue},
                          attentionborder=1pt,
                          attentionBorderColor={named}{Crimson},
                          attentionBgColor={named}{MistyRose},
                       ''',
}

latex_appendices = ['floats', 'unicode']
latex_domain_indices = False


