# -*- coding: utf-8 -*-

"""
Created on 2018-05-12
:author: {{cookiecutter.full_name}} ({{cookiecutter.email}})
"""

from kotti.interfaces import IDefaultWorkflow
from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from zope.interface import implements

from {{cookiecutter.project_slug}} import _


class CustomContent(Content):
    """ A custom content type. """

    implements(IDefaultWorkflow)

    id = Column(ForeignKey('contents.id'), primary_key=True)
    custom_attribute = Column(Unicode(1000))

    type_info = Content.type_info.copy(
        name=u'CustomContent',
        title=_(u'CustomContent'),
        add_view=u'add_custom_content',
        addable_to=[u'Document'],
        selectable_default_views=[
            ("alternative-view", _(u"Alternative view")),
        ],
    )

    def __init__(self, custom_attribute=None, **kwargs):
        """ Constructor

        :param custom_attribute: A very custom attribute
        :type custom_attribute: unicode

        :param **kwargs: Arguments that are passed to the base class(es)
        :type **kwargs: see :class:`kotti.resources.Content`
        """

        super(CustomContent, self).__init__(**kwargs)

        self.custom_attribute = custom_attribute
