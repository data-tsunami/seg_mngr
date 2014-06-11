# -*- coding: utf-8 -*-
#@PydevCodeAnalysisIgnore
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Server.address_ip'
        db.delete_column(u'seg_mngr_server', 'address_ip_id')

        # Adding field 'ConfigIp.server'
        db.add_column(u'seg_mngr_configip', 'server',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['seg_mngr.Server']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Server.address_ip'
        db.add_column(u'seg_mngr_server', 'address_ip',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['seg_mngr.ConfigIp']),
                      keep_default=False)

        # Deleting field 'ConfigIp.server'
        db.delete_column(u'seg_mngr_configip', 'server_id')


    models = {
        u'seg_mngr.configip': {
            'Meta': {'object_name': 'ConfigIp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Server']"})
        },
        u'seg_mngr.server': {
            'Meta': {'object_name': 'Server'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['seg_mngr']