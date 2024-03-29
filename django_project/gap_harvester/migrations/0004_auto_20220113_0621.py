# Generated by Django 3.2.8 on 2022-01-13 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gap_data', '0017_alter_geometryuploaderfile_file'),
        ('gap_harvester', '0003_alter_harvester_harvester_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvester',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='harvester',
            name='user',
            field=models.ForeignKey(blank=True, help_text='User who run the harvester.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='harvesterattribute',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='harvester/attributes'),
        ),
        migrations.AlterField(
            model_name='harvester',
            name='harvester_class',
            field=models.CharField(choices=[('gap_harvester.harveters.api_with_geography_and_today_date.APIWithGeographyAndTodayDate', 'API With Geography Using Today Date'), ('gap_harvester.harveters.api_with_geography_and_date.APIWithGeographyAndDate', 'API With Geography And Date'), ('gap_harvester.harveters.using_exposed_api.UsingExposedAPI', 'Harvested using exposed API by external client'), ('gap_harvester.harveters.excel_harvester.ExcelHarvester', 'Excel Harvesters')], help_text='The type of harvester that will be used.Use class with full package.', max_length=256),
        ),
        migrations.AlterField(
            model_name='harvester',
            name='indicator',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gap_data.indicator'),
        ),
    ]
