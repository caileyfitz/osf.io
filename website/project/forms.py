# -*- coding: utf-8 -*-
from framework import Form, TextField, TextAreaField, validators
from framework.forms import BootstrapTextArea, BootstrapTextInput

###############################################################################
# Forms
###############################################################################

class NewProjectForm(Form):
    title    = TextField('Title', [
        validators.Required(message=u'Title is required'),
        validators.Length(min=1, message=u'Title is too short.(It must have at least 1 character.)'),
        validators.Length(max=200, message=u'Title is too long.(It must have at least 200 characters.)')
    ], widget=BootstrapTextInput())
    description    = TextAreaField('Description', widget=BootstrapTextArea())

class NewNodeForm(Form):
    title    = TextField('Title', [
        validators.Required(message=u'Title is required'),
        validators.Length(min=1, message=u'Title is too short.(It must have at least 1 character.)'),
        validators.Length(max=200, message=u'Title is too long.(It must have at least 200 characters.)')
    ], widget=BootstrapTextInput())
    description     = TextAreaField('Description', widget=BootstrapTextArea())
    category        = TextAreaField('Category', widget=BootstrapTextArea())
