# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'History.checksum'
        db.alter_column(u'gitlab_logging_history', 'checksum', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40))
        # Adding unique constraint on 'History', fields ['checksum']
        db.create_unique(u'gitlab_logging_history', ['checksum'])

        # Adding index on 'History', fields ['iid']
        db.create_index(u'gitlab_logging_history', ['iid'])


    def backwards(self, orm):
        # Removing index on 'History', fields ['iid']
        db.delete_index(u'gitlab_logging_history', ['iid'])

        # Removing unique constraint on 'History', fields ['checksum']
        db.delete_unique(u'gitlab_logging_history', ['checksum'])


        # Changing field 'History.checksum'
        db.alter_column(u'gitlab_logging_history', 'checksum', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'gitlab_logging.history': {
            'Meta': {'object_name': 'History'},
            'checksum': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['gitlab_logging']