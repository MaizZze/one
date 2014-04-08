# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Statistic.parent'
        db.alter_column(u'one_app_statistic', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['one_app.Statistic']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Statistic.parent'
        raise RuntimeError("Cannot reverse this migration. 'Statistic.parent' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Statistic.parent'
        db.alter_column(u'one_app_statistic', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['one_app.Statistic']))

    models = {
        u'one_app.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'one_app.property': {
            'Meta': {'object_name': 'Property'},
            'groups': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': u"orm['one_app.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'one_app.statistic': {
            'Meta': {'object_name': 'Statistic'},
            'falseCount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'statistics'", 'null': 'True', 'to': u"orm['one_app.Statistic']"}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statistics'", 'to': u"orm['one_app.Property']"}),
            'trueCount': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['one_app']