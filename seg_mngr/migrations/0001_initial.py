# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConfigIp'
        db.create_table(u'seg_mngr_configip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'seg_mngr', ['ConfigIp'])

        # Adding model 'Server'
        db.create_table(u'seg_mngr_server', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address_ip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seg_mngr.ConfigIp'])),
            ('operating_system', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'seg_mngr', ['Server'])


    def backwards(self, orm):
        # Deleting model 'ConfigIp'
        db.delete_table(u'seg_mngr_configip')

        # Deleting model 'Server'
        db.delete_table(u'seg_mngr_server')


    models = {
        u'seg_mngr.configip': {
            'Meta': {'object_name': 'ConfigIp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'seg_mngr.server': {
            'Meta': {'object_name': 'Server'},
            'address_ip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.ConfigIp']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['seg_mngr']