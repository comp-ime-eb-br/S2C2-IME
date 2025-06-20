# Generated by Django 3.2.6 on 2022-02-14 21:38

from django.db import migrations, models
import django.db.models.deletion
import provenanceCatcher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experimenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_content', provenanceCatcher.models.XMLField(blank=True, null=True)),
                ('round', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='experimenter.round')),
            ],
            options={
                'db_table': 'Result',
            },
        ),
    ]
