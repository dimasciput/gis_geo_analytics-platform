# Generated by Django 3.2.8 on 2021-11-04 08:27

from django.db import migrations, models
import django.db.models.deletion
import gap_data.models.geometry
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gap_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeometryUploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('file', models.FileField(upload_to='upload')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='instance',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='geometry',
            name='active_date_from',
            field=models.DateField(default=gap_data.models.geometry.default_active_date_from),
        ),
        migrations.AddField(
            model_name='geometry',
            name='active_date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='geometry',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='GeometryUploaderLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=512)),
                ('note', models.TextField(blank=True, null=True)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gap_data.geometryuploader')),
            ],
        ),
    ]
