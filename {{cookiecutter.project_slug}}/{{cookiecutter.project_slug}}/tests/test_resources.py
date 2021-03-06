# -*- coding: utf-8 -*-

"""
Created on {% now 'local', '%Y-%m-%d' %}
:author: {{cookiecutter.full_name}} ({{cookiecutter.email}})
"""

from pytest import raises


def test_model(root, db_session):
    from {{cookiecutter.project_slug}}.resources import CustomContent

    cc = CustomContent()
    assert cc.custom_attribute is None

    cc = CustomContent(custom_attribute=u'Foo')
    assert cc.custom_attribute == u'Foo'

    root['cc'] = cc = CustomContent()
    assert cc.name == 'cc'

    with raises(TypeError):
        cc = CustomContent(doesnotexist=u'Foo')
