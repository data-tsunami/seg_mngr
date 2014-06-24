# -*- coding: utf-8 -*-

from django import forms
from seg_mngr.models import ServerTask, OperatingSystem, CrossCheck, Task


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
        CHOICES.extend(choices)
        self.fields['operating_system'].choices = CHOICES


class CrossCheckForm(forms.ModelForm):

    class Meta:
        model = CrossCheck
        fields = ('success', 'tasks')


class CrossCheckTaskSelectionForm(forms.Form):

    tasks = forms.MultipleChoiceField(label="Tareas", choices=(),
        help_text="Seleccione 1 ó mas tareas")

    def __init__(self, *args, **kwargs):
        super(CrossCheckTaskSelectionForm, self).__init__(*args, **kwargs)
        choices = [(os.id, unicode(os)) for os in
                   Task.objects.all()]
        self.fields['tasks'].choices = choices
