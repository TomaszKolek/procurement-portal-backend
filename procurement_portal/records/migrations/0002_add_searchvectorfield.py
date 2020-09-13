# Generated by Django 2.2.16 on 2020-09-13 12:15

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    migration = '''
        CREATE TRIGGER records_purchaserecord_content_search_update BEFORE INSERT OR UPDATE
        ON records_purchaserecord FOR EACH ROW EXECUTE PROCEDURE
        tsvector_update_trigger(
            full_text_search, 'pg_catalog.english',
            supplier_name
         );

        -- Force triggers to run and populate the text_search column.
        UPDATE records_purchaserecord set ID = ID;
    '''

    reverse_migration = '''
        DROP TRIGGER records_purchaserecord_full_text_search ON records_purchaserecord;
    '''

    operations = [
        migrations.AddField(
            model_name='purchaserecord',
            name='full_text_search',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.RunSQL(migration, reverse_migration)
    ]
