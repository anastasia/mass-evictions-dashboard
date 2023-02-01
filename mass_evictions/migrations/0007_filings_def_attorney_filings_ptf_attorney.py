# Generated by Django 4.1.5 on 2023-02-01 20:52

from django.db import migrations, models
import django.db.models.deletion

def add_bars(apps, schema_editor):
    Attorneys = apps.get_model("mass_evictions", "Attorneys")
    Filings = apps.get_model("mass_evictions", "Filings")
    for filing in Filings.objects.all():
        if filing.ptf_bar_str:
            ptf_attorney, created = Attorneys.objects.get_or_create(bar=filing.ptf_bar_str)
            filing.ptf_attorney = ptf_attorney
            if created:
                print("ptf created", filing.ptf_bar_str)
        if filing.def_bar_str:
            def_attorney, created = Attorneys.objects.get_or_create(bar=filing.def_bar_str)
            filing.def_attorney = def_attorney
            if created:
                print("def created", filing.def_bar_str)

        filing.save()

def remove_bars(apps, schema_editor):
    Filings = apps.get_model("mass_evictions", "Filings")
    for filing in Filings.objects.all():
        filing.ptf_bar_str = filing.ptf_attorney.bar
        filing.def_bar_str = filing.def_attorney.bar
        filing.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mass_evictions', '0006_rename_def_bar_filings_def_bar_str_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filings',
            name='def_attorney',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='filing_defendant_attorney', to='mass_evictions.attorneys'),
        ),
        migrations.AddField(
            model_name='filings',
            name='ptf_attorney',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='filing_plaintiff_attorney', to='mass_evictions.attorneys'),
        ),
        migrations.RunPython(add_bars, remove_bars),
    ]
