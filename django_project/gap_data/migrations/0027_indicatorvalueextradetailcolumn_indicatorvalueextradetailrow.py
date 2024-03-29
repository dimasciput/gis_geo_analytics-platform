# Generated by Django 3.2.8 on 2022-03-16 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gap_data', '0026_alter_indicator_access_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorValueExtraDetailRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gap_data.indicatorvalue')),
            ],
        ),
        migrations.CreateModel(
            name='IndicatorValueExtraDetailColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of column', max_length=100)),
                ('value', models.TextField(default=True, help_text='The value of cell', null=True)),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gap_data.indicatorvalueextradetailrow')),
            ],
            options={
                'unique_together': {('row', 'name')},
            },
        ),
    ]
