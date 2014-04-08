# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Group.style'
        db.add_column(u'one_app_group', 'style',
                      self.gf('django.db.models.fields.CharField')(default='panel-primary', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Group.style'
        db.delete_column(u'one_app_group', 'style')


    models = {
        u'one_app.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'panel-primary'", 'max_length': '100'})
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