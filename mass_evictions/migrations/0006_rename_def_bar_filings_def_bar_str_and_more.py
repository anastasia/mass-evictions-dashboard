# Generated by Django 4.1.5 on 2023-02-01 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mass_evictions', '0005_bar_to_fk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filings',
            old_name='def_bar',
            new_name='def_bar_str',
        ),
        migrations.RenameField(
            model_name='filings',
            old_name='ptf_bar',
            new_name='ptf_bar_str',
        ),
    ]
