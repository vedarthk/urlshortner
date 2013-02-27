# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shortener'
        db.create_table('shortner_shortener', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=2047)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('shortcode', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
        ))
        db.send_create_signal('shortner', ['Shortener'])


    def backwards(self, orm):
        # Deleting model 'Shortener'
        db.delete_table('shortner_shortener')


    models = {
        'shortner.shortener': {
            'Meta': {'object_name': 'Shortener'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'shortcode': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '2047'})
        }
    }

    complete_apps = ['shortner']