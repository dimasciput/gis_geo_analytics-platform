# Generated by Django 3.2.8 on 2022-03-17 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rir_harvester', '0006_harvesterlog_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvester',
            name='harvester_class',
            field=models.CharField(choices=[('rir_harvester.harveters.api_with_geography_and_today_date.APIWithGeographyAndTodayDate', 'API With Geography Using Today Date'), ('rir_harvester.harveters.api_with_geography_and_date.APIWithGeographyAndDate', 'API With Geography And Date'), ('rir_harvester.harveters.sharepoint_harvester.SharepointHarvester', 'Sharepoint File'), ('rir_harvester.harveters.using_exposed_api.UsingExposedAPI', 'Harvested using exposed API by external client'), ('rir_harvester.harveters.excel_harvester.ExcelHarvester', 'Excel Harvesters'), ('rir_harvester.harveters.etools.program_coverage.EtoolsProgramCoverageHarvester', 'Etools : Program coverage')], help_text='The type of harvester that will be used.Use class with full package.', max_length=256),
        ),
    ]
