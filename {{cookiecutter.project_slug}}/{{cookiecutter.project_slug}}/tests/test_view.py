# -*- coding: utf-8 -*-

"""
Created on {% now 'local', '%Y-%m-%d' %}
:author: {{cookiecutter.full_name}} ({{cookiecutter.email}})
"""

from pytest import fixture


@fixture
def dummy_content(root):

    from {{cookiecutter.project_slug}}.resources import CustomContent

    root['cc'] = cc = CustomContent(
        title=u'My content',
        description=u'My very custom content is custom',
        custom_attribute='Lorem ipsum'
    )

    return cc


def test_view(dummy_content, dummy_request):

    from {{cookiecutter.project_slug}}.views.view import CustomContentViews

    views = CustomContentViews(dummy_content, dummy_request)

    default = views.default_view()
    assert 'foo' in default

    alternative = views.alternative_view()
    assert alternative['foo'] == u'bar'
