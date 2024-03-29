# Generated by Django 3.2.8 on 2022-01-04 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gap_data', '0011_basemaplayer_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.CharField(max_length=256)),
                ('is_public', models.BooleanField(default=True, help_text='Is the link available for public or just admin.')),
                ('order', models.IntegerField(default=0)),
                ('instance', models.ForeignKey(blank=True, help_text='Make this empty to be used by every instance.', null=True, on_delete=django.db.models.deletion.CASCADE, to='gap_data.instance')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
