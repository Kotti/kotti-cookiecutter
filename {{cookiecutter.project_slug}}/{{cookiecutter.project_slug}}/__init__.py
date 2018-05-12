# -*- coding: utf-8 -*-

"""
Created on 2018-05-12
:author: {{cookiecutter.full_name}} ({{cookiecutter.email}})
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('{{cookiecutter.project_slug}}')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                {{cookiecutter.project_slug}}.kotti_configure

        to enable the ``{{cookiecutter.project_slug}}`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' {{cookiecutter.project_slug}}'
    settings['kotti.alembic_dirs'] += ' {{cookiecutter.project_slug}}:alembic'
    settings['kotti.available_types'] += ' {{cookiecutter.project_slug}}.resources.CustomContent'
    settings['kotti.fanstatic.view_needed'] += ' {{cookiecutter.project_slug}}.fanstatic.css_and_js'
    File.type_info.addable_to.append('CustomContent')


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('{{cookiecutter.project_slug}}:locale')
    config.add_static_view('static-{{cookiecutter.project_slug}}', '{{cookiecutter.project_slug}}:static')

    config.scan(__name__)
