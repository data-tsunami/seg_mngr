# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CrossCheckTask'
        db.create_table(u'seg_mngr_crosschecktask', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cross_check', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seg_mngr.CrossCheck'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seg_mngr.Task'])),
            ('success', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'seg_mngr', ['CrossCheckTask'])

        # Removing M2M table for field task on 'CrossCheck'
        db.delete_table(db.shorten_name(u'seg_mngr_crosscheck_task'))


    def backwards(self, orm):
        # Deleting model 'CrossCheckTask'
        db.delete_table(u'seg_mngr_crosschecktask')

        # Adding M2M table for field task on 'CrossCheck'
        m2m_table_name = db.shorten_name(u'seg_mngr_crosscheck_task')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crosscheck', models.ForeignKey(orm[u'seg_mngr.crosscheck'], null=False)),
            ('task', models.ForeignKey(orm[u'seg_mngr.task'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crosscheck_id', 'task_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'seg_mngr.configip': {
            'Meta': {'object_name': 'ConfigIp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Server']"})
        },
        u'seg_mngr.crosscheck': {
            'Meta': {'object_name': 'CrossCheck'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'check_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Server']"}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tasks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['seg_mngr.Task']", 'through': u"orm['seg_mngr.CrossCheckTask']", 'symmetrical': 'False'})
        },
        u'seg_mngr.crosschecktask': {
            'Meta': {'object_name': 'CrossCheckTask'},
            'cross_check': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.CrossCheck']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Task']"})
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
        u'seg_mngr.periodictask': {
            'Meta': {'object_name': 'PeriodicTask'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'frecuency': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'server': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['seg_mngr.Server']", 'symmetrical': 'False', 'blank': 'True'})
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
            'autor_update_state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'comments': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'date_update_state': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'server': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seg_mngr.Server']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "u'P'", 'max_length': '64'}),
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