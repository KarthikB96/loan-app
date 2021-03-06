# Generated by Django 3.1 on 2020-08-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationdata',
            old_name='credit_history',
            new_name='creditHistory',
        ),
        migrations.RenameField(
            model_name='applicationdata',
            old_name='entity_type',
            new_name='entityType',
        ),
        migrations.RenameField(
            model_name='applicationdata',
            old_name='filter_id',
            new_name='filterId',
        ),
        migrations.RenameField(
            model_name='applicationdata',
            old_name='loan_amount',
            new_name='loanAmount',
        ),
        migrations.RenameField(
            model_name='owners',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='business',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='owners',
            name='homePhone',
            field=models.CharField(max_length=200),
        ),
    ]
