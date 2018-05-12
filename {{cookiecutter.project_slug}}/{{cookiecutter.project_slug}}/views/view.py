# -*- coding: utf-8 -*-

"""
Created on 2018-05-12
:author: {{cookiecutter.full_name}} ({{cookiecutter.email}})
"""

from pyramid.view import view_config
from pyramid.view import view_defaults

from {{cookiecutter.project_slug}} import _
from {{cookiecutter.project_slug}}.resources import CustomContent
from {{cookiecutter.project_slug}}.fanstatic import css_and_js
from {{cookiecutter.project_slug}}.views import BaseView


@view_defaults(context=CustomContent, permission='view')
class CustomContentViews(BaseView):
    """ Views for :class:`{{cookiecutter.project_slug}}.resources.CustomContent` """

    @view_config(name='view', permission='view',
                 renderer='{{cookiecutter.project_slug}}:templates/custom-content-default.pt')
    def default_view(self):
        """ Default view for :class:`{{cookiecutter.project_slug}}.resources.CustomContent`

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        return {
            'foo': _(u'bar'),
        }

    @view_config(name='alternative-view', permission='view',
                 renderer='{{cookiecutter.project_slug}}:templates/custom-content-alternative.pt')
    def alternative_view(self):
        """ Alternative view for :class:`{{cookiecutter.project_slug}}.resources.CustomContent`.
        This view requires the JS / CSS resources defined in
        :mod:`{{cookiecutter.project_slug}}.fanstatic`.

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        css_and_js.need()

        return {
            'foo': _(u'bar'),
        }
