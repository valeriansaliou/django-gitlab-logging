# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'History.iid'
        db.add_column(u'gitlab_logging_history', 'iid',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'History.iid'
        db.delete_column(u'gitlab_logging_history', 'iid')


    models = {
        u'gitlab_logging.history': {
            'Meta': {'object_name': 'History'},
            'checksum': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iid': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['gitlab_logging']