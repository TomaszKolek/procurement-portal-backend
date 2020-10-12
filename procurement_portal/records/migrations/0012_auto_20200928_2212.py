# Generated by Django 3.1.1 on 2020-09-28 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_purchaserecord_bbbee_status'),
    ]

    migration = '''
        DROP TRIGGER IF EXISTS full_text_search_content_update ON records_purchaserecord;

        -- Force triggers to run and populate the text_search column.
        UPDATE records_purchaserecord set ID = ID;
    '''

    reverse_migration = '''
        CREATE TRIGGER full_text_search_content_update BEFORE INSERT OR UPDATE
        ON records_purchaserecord FOR EACH ROW EXECUTE PROCEDURE
        tsvector_update_trigger(
            full_text_search, 'pg_catalog.english',
            supplier_name, buyer_name, central_supplier_database_number, company_registration_number, director_names, director_names_and_surnames, director_surnames, implementation_location, implementation_location_district_municipality, implementation_location_facility, implementation_location_local_municipality, implementation_location_other, implementation_location_province, items_description, items_quantity
        );

        -- Force triggers to run and populate the text_search column.
        UPDATE records_purchaserecord set ID = ID;
    '''

    operations = [
        migrations.RunSQL(migration, reverse_migration),
        migrations.RemoveIndex(
            model_name='purchaserecord',
            name='records_pur_full_te_99a9e9_gin',
        ),
        migrations.RemoveField(
            model_name='purchaserecord',
            name='full_text_search',
        ),
    ]