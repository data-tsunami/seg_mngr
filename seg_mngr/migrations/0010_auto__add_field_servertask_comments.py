# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ServerTask.comments'
        db.add_column(u'seg_mngr_servertask', 'comments',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ServerTask.comments'
        db.delete_column(u'seg_mngr_servertask', 'comments')


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
            'nivel_exposicion': ('django.db.models.fields.IntegerField', [], {'default': '3', 'max_length': '2'}),
            'operating_system': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.OperatingSystem']"}),
            'task': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['seg_mngr.Task']", 'symmetrical': 'False', 'through': u"orm['seg_mngr.ServerTask']", 'blank': 'True'})
        },
        u'seg_mngr.servertask': {
            'Meta': {'object_name': 'ServerTask'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Server']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '64'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Task']"})
        },
        u'seg_mngr.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'task_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.TaskGroup']"})
        },
        u'seg_mngr.taskgroup': {
            'Meta': {'object_name': 'TaskGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['seg_mngr']