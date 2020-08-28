# Generated by Django 3.1 on 2020-08-26 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.IntegerField(max_length=5)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='RequestHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CFRequestId', models.IntegerField()),
                ('requestDate', models.DateTimeField()),
                ('CFApiUserId', models.CharField(max_length=50)),
                ('CFApiPassword', models.CharField(max_length=50)),
                ('isTestLead', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('dateOfBirth', models.DateTimeField()),
                ('homePhone', models.CharField(max_length=12)),
                ('ssn', models.CharField(max_length=200)),
                ('percentageOfOwnership', models.FloatField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.address')),
            ],
            options={
                'db_table': 'owners',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('annualRevenue', models.FloatField()),
                ('averageBankBalance', models.FloatField()),
                ('averageCreditCardVolume', models.FloatField()),
                ('taxId', models.IntegerField(blank=True)),
                ('phone', models.IntegerField(blank=True)),
                ('naics', models.IntegerField(blank=True)),
                ('profitable', models.BooleanField()),
                ('bankrupted', models.BooleanField()),
                ('inceptionDate', models.DateField()),
                ('updated', models.BooleanField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.address')),
                ('owners', models.ManyToManyField(to='backendapp.Owners')),
            ],
            options={
                'db_table': 'business',
            },
        ),
        migrations.CreateModel(
            name='ApplicationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.FloatField()),
                ('credit_history', models.IntegerField()),
                ('entity_type', models.CharField(max_length=200)),
                ('filter_id', models.IntegerField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.business')),
            ],
            options={
                'db_table': 'applicationdata',
            },
        ),
    ]