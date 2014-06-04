# -*- coding: utf-8 -*-

from django import forms
from seg_mngr.models import ServerTask, OperatingSystem


# Formulario de modelo ServerTask
class ServerTaskForm(forms.ModelForm):

    class Meta:
        model = ServerTask
        fields = ('comments',)


class ServerSearchForm(forms.Form):

    operating_system = forms.ChoiceField(label="Operating System", choices=(),
                        widget=forms.Select(attrs={'class': 'selector'}))

    def __init__(self, *args, **kwargs):
        CHOICES = [
            (0, "ALL Operating Systems"),
        ]
        super(ServerSearchForm, self).__init__(*args, **kwargs)
        choices = [(os.id, unicode(os)) for os in
                   OperatingSystem.objects.all()]
        choices.extend(CHOICES)
        self.fields['operating_system'].choices = choices
