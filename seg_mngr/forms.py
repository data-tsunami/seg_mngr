# -*- coding: utf-8 -*-

from django import forms
from seg_mngr.models import ServerTask


# Formulario de modelo ServerTask
class ServerTaskForm(forms.ModelForm):

    class Meta:
        model = ServerTask
        fields = ('comments',) 