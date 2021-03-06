'''
Created on 29/05/2014

@author: federico
'''
# -*- coding: utf-8 -*-
from seg_mngr.models import ServerTask, Server


def server_task_state(request):

    return {
        'PENDIENTE': ServerTask.PENDIENTE,
        'NO_APLICA': ServerTask.NO_APLICA,
        'EN_CURSO': ServerTask.EN_CURSO,
        'FINALIZADA': ServerTask.FINALIZADA}


def server_nivel_exposicion(request):

    return {
            'PUBLICO':Server.PUBLICO,
            'NAT':Server.NAT,
            'LAN':Server.LAN
            }