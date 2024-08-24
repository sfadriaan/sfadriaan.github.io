# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Salesforce Adriaan'
html_title = 'Salesforce Adriaan'
copyright = '2024, Adriaan van Niekerk'
author = 'Adriaan van Niekerk'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','.venv']
extensions = [
    "sphinx_inline_tabs"
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_context = {

    # Change to the link to your product website (without "https://")
    #'product_page': '',

    # Add your product tag to ".sphinx/_static" and change the path
    # here (start with "_static"), default is the circle of friends
    # XXX 2023-09-29: jugmac00 - currently using the Canonical default image
    #'product_tag': '_static/tag.png',

    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    'discourse': '',

    # Change to the GitHub info for your project
    'github_url': 'https://github.com/sfadriaan/sfadriaan.github.io',

    # Change to the branch for this version of the documentation
    'github_version': 'master',

    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    'github_folder': '/',

    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    'github_issues': 'enabled',

    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    'sequential_nav': "none"
}

