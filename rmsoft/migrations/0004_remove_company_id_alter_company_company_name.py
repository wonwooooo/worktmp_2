# Generated by Django 4.1.4 on 2022-12-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmsoft', '0003_alter_client_client_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
