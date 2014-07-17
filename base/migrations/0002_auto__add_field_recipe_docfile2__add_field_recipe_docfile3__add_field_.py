# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.docfile2'
        db.add_column(u'base_recipe', 'docfile2',
                      self.gf('django.db.models.fields.files.FileField')(default='recipes/no-img.jpg', max_length=100),
                      keep_default=False)

        # Adding field 'Recipe.docfile3'
        db.add_column(u'base_recipe', 'docfile3',
                      self.gf('django.db.models.fields.files.FileField')(default='recipes/no-img.jpg', max_length=100),
                      keep_default=False)

        # Adding field 'Recipe.docfile4'
        db.add_column(u'base_recipe', 'docfile4',
                      self.gf('django.db.models.fields.files.FileField')(default='recipes/no-img.jpg', max_length=100),
                      keep_default=False)

        # Adding field 'Recipe.docfile5'
        db.add_column(u'base_recipe', 'docfile5',
                      self.gf('django.db.models.fields.files.FileField')(default='recipes/no-img.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recipe.docfile2'
        db.delete_column(u'base_recipe', 'docfile2')

        # Deleting field 'Recipe.docfile3'
        db.delete_column(u'base_recipe', 'docfile3')

        # Deleting field 'Recipe.docfile4'
        db.delete_column(u'base_recipe', 'docfile4')

        # Deleting field 'Recipe.docfile5'
        db.delete_column(u'base_recipe', 'docfile5')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'base.hostedmeal': {
            'Meta': {'object_name': 'HostedMeal'},
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'did_you_host_the_meal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'host'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_pickup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_sitdown': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'maximum_diners_allowed': ('django.db.models.fields.IntegerField', [], {}),
            'meal_purchases': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.MealPurchase']", 'symmetrical': 'False', 'blank': 'True'}),
            'minimum_diners_required': ('django.db.models.fields.IntegerField', [], {}),
            'price_per_serving': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Recipe']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'base.hostedmealreview': {
            'Meta': {'object_name': 'HostedMealReview'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'did_the_hosted_meal_happen': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'did_you_show_up': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hosted_meal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.HostedMeal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'base.hostsreviewofdiners': {
            'Meta': {'object_name': 'HostsReviewOfDiners'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'did_they_show_up': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'hosted_meal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.HostedMeal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'base.mealpurchase': {
            'Meta': {'object_name': 'MealPurchase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchaser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'base.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'docfile': ('django.db.models.fields.files.FileField', [], {'default': "'recipes/no-img.jpg'", 'max_length': '100'}),
            'docfile2': ('django.db.models.fields.files.FileField', [], {'default': "'recipes/no-img.jpg'", 'max_length': '100'}),
            'docfile3': ('django.db.models.fields.files.FileField', [], {'default': "'recipes/no-img.jpg'", 'max_length': '100'}),
            'docfile4': ('django.db.models.fields.files.FileField', [], {'default': "'recipes/no-img.jpg'", 'max_length': '100'}),
            'docfile5': ('django.db.models.fields.files.FileField', [], {'default': "'recipes/no-img.jpg'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dairy_free': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_gluten_free': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_nut_free': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_vegan': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_vegetarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'base.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'docfile': ('django.db.models.fields.files.FileField', [], {'default': "'profiles/no-img.jpg'", 'max_length': '100', 'blank': 'True'}),
            'estimated_latitude': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '11', 'decimal_places': '8'}),
            'estimated_longitude': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '11', 'decimal_places': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_first_time': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'paypal_payout_email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'remind_me_later': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'upcooking_score': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['base']