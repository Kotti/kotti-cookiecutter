# -*- coding: utf-8 -*-

"""
Created on 2018-05-12
:author: AUTHOR_NAME (AUTHOR_EMAIL@email.com)
"""

from __future__ import absolute_import, division, print_function

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource


library = Library("{{cookiecutter.project_slug}}", "static")

css = Resource(
    library,
    "styles.css",
    minified="styles.min.css")
js = Resource(
    library,
    "scripts.js",
    minified="scripts.min.js")

css_and_js = Group([css, js])
