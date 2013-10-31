# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'History.iid'
        db.delete_column(u'gitlab_logging_history', 'iid')

        # Adding field 'History.project_id'
        db.add_column(u'gitlab_logging_history', 'project_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Adding field 'History.issue_id'
        db.add_column(u'gitlab_logging_history', 'issue_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'History.iid'
        db.add_column(u'gitlab_logging_history', 'iid',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None, db_index=True),
                      keep_default=False)

        # Deleting field 'History.project_id'
        db.delete_column(u'gitlab_logging_history', 'project_id')

        # Deleting field 'History.issue_id'
        db.delete_column(u'gitlab_logging_history', 'issue_id')


    models = {
        u'gitlab_logging.history': {
            'Meta': {'object_name': 'History'},
            'checksum': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'project_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['gitlab_logging']