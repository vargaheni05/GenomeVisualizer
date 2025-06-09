from GenomeVisualizer import __version__

project = 'GenomeVisualizer'
copyright = '2025, Varga Henrietta'
author = 'Varga Henrietta'
release = __version__

extensions = ['sphinx.ext.autodoc','sphinx.ext.napoleon','sphinx.ext.viewcode','sphinx_toolbox.more_autodoc.autotypeddict','enum_tools.autoenum']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    "display_github": True
}

html_theme_options = {
    'logo_only': False,
    'vcs_pageview_mode': ''
}
