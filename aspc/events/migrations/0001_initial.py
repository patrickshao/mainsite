# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(default='pending', max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True))
        ))
        db.send_create_signal('events', ['Event'])

        # Adding model 'FacebookEventPage'
        db.create_table('events_facebookeventpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('page_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('events', ['FacebookEventPage'])

    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('events_event')

        # Deleting model 'FacebookEventPage'
        db.delete_table('events_facebookeventpage')

    models = {
            'events.event': {
                'Meta': {'ordering': "('start', 'name', 'end')", 'object_name': 'Event'},
                'description': ('django.db.models.fields.TextField', [], {}),
                'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
                'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
                'start': ('django.db.models.fields.DateTimeField', [], {}),
                'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '255'}),
                'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
            },
            'events.facebookeventpage': {
                'Meta': {'object_name': 'FacebookEventPage'},
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
                'url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
                'page_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
            }
        }

    complete_apps = ['events']