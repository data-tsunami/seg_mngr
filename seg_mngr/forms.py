# -*- coding: utf-8 -*-

from django import forms
from django.db.models import Q
from seg_mngr.models import ServerTask, OperatingSystem, Server, Task


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


class CrossCheckTaskSelectionForm(forms.Form):

    tasks = forms.MultipleChoiceField(label="Tareas", choices=(),
        help_text="Seleccione 1 ó mas tareas")

    def __init__(self, *args, **kwargs):
        self.server = kwargs.get('server', None)
        if kwargs['server'] is not None:
            del kwargs['server']
        super(CrossCheckTaskSelectionForm, self).__init__(*args, **kwargs)
        servidor = Server.objects.get(pk=self.server)
        tasks_dic = ServerTask.objects.values('task').filter(
            Q(server=servidor.id), Q(state=ServerTask.FINALIZADA) |
            Q(state=ServerTask.NO_APLICA))
        tasks = []
        for tarea in tasks_dic:
            task = Task.objects.get(pk=tarea['task'])
            tasks.append(task)
        choices = [(os.id, unicode(os)) for os in
                   tasks]
        self.fields['tasks'].choices = choices
