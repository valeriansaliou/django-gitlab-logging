# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'History'
        db.create_table(u'gitlab_logging_history', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checksum', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'gitlab_logging', ['History'])


    def backwards(self, orm):
        # Deleting model 'History'
        db.delete_table(u'gitlab_logging_history')


    models = {
        u'gitlab_logging.history': {
            'Meta': {'object_name': 'History'},
            'checksum': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['gitlab_logging']