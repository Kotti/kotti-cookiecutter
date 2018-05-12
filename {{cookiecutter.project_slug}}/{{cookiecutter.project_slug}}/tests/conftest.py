# -*- coding: utf-8 -*-

"""
Created on 2018-05-12
:author: AUTHOR_NAME (AUTHOR_EMAIL@email.com)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import {{cookiecutter.project_slug}}.resources
    {{cookiecutter.project_slug}}.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               '{{cookiecutter.project_slug}}.kotti_configure'}
