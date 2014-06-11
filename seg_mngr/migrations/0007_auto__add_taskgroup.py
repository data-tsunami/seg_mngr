# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TaskGroup'
        db.create_table(u'seg_mngr_taskgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'seg_mngr', ['TaskGroup'])


    def backwards(self, orm):
        # Deleting model 'TaskGroup'
        db.delete_table(u'seg_mngr_taskgroup')


    models = {
        u'seg_mngr.configip': {
            'Meta': {'object_name': 'ConfigIp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Server']"})
        },
        u'seg_mngr.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'seg_mngr.operatingsystem': {
            'Meta': {'object_name': 'OperatingSystem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'seg_mngr.server': {
            'Meta': {'object_name': 'Server'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'operating_system': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.OperatingSystem']"}),
            'task': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['seg_mngr.Task']", 'symmetrical': 'False', 'through': u"orm['seg_mngr.ServerTask']", 'blank': 'True'})
        },
        u'seg_mngr.servertask': {
            'Meta': {'object_name': 'ServerTask'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Server']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '64'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Task']"})
        },
        u'seg_mngr.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'seg_mngr.taskgroup': {
            'Meta': {'object_name': 'TaskGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['seg_mngr']