# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'storefront_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('category_id', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shop', to=orm['storefront.Shop'])),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'storefront', ['Item'])

        # Adding model 'Shop'
        db.create_table(u'storefront_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('shop_id', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('announcement', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'storefront', ['Shop'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'storefront_item')

        # Deleting model 'Shop'
        db.delete_table(u'storefront_shop')


    models = {
        u'storefront.item': {
            'Meta': {'object_name': 'Item'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shop'", 'to': u"orm['storefront.Shop']"}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'storefront.shop': {
            'Meta': {'object_name': 'Shop'},
            'announcement': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'shop_id': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['storefront']