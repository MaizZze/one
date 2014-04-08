# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'one_app_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'one_app', ['Group'])

        # Adding model 'Property'
        db.create_table(u'one_app_property', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('groups', self.gf('django.db.models.fields.related.ForeignKey')(related_name='properties', to=orm['one_app.Group'])),
        ))
        db.send_create_signal(u'one_app', ['Property'])

        # Adding model 'Statistic'
        db.create_table(u'one_app_statistic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statistics', to=orm['one_app.Property'])),
            ('trueCount', self.gf('django.db.models.fields.IntegerField')()),
            ('falseCount', self.gf('django.db.models.fields.IntegerField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statistics', to=orm['one_app.Statistic'])),
        ))
        db.send_create_signal(u'one_app', ['Statistic'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'one_app_group')

        # Deleting model 'Property'
        db.delete_table(u'one_app_property')

        # Deleting model 'Statistic'
        db.delete_table(u'one_app_statistic')


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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statistics'", 'to': u"orm['one_app.Statistic']"}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statistics'", 'to': u"orm['one_app.Property']"}),
            'trueCount': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['one_app']