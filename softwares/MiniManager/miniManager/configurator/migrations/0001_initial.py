# Generated by Django 3.2.6 on 2022-02-14 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicao_schema', models.TextField()),
                ('stop_time', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'Configuration',
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Interface',
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Measures',
            },
        ),
        migrations.CreateModel(
            name='MModelCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('displayname', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'MModelCatalog',
            },
        ),
        migrations.CreateModel(
            name='MobilityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.mmodelcatalog')),
            ],
            options={
                'db_table': 'MobilityModel',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noise_th', models.IntegerField(default=-91)),
                ('fading_cof', models.IntegerField(default=0)),
                ('adhoc', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Network',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mac', models.CharField(max_length=30)),
                ('type', models.CharField(blank=True, max_length=30, null=True)),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.network')),
            ],
            options={
                'db_table': 'Node',
            },
        ),
        migrations.CreateModel(
            name='PerformanceMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('unit', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'PerformanceMeasure',
            },
        ),
        migrations.CreateModel(
            name='PModelCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('displayname', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'PModelCatalog',
            },
        ),
        migrations.CreateModel(
            name='PropagationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.pmodelcatalog')),
            ],
            options={
                'db_table': 'PropagationModel',
            },
        ),
        migrations.CreateModel(
            name='TestPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(null=True)),
                ('author', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'TestPlan',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('configuration', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurator.configuration')),
                ('test_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configurator.testplan')),
            ],
            options={
                'db_table': 'Version',
            },
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='configurator.node')),
            ],
            options={
                'db_table': 'Switch',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='configurator.node')),
            ],
            options={
                'db_table': 'Station',
            },
        ),
        migrations.CreateModel(
            name='PropagationParam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.FloatField()),
                ('propagationmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.propagationmodel')),
            ],
            options={
                'db_table': 'PropagationParam',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.node')),
            ],
            options={
                'db_table': 'Position',
            },
        ),
        migrations.CreateModel(
            name='PerformanceMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
                ('source', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=20)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.configuration')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.performancemeasure')),
            ],
            options={
                'db_table': 'PerformanceMeasurement',
            },
        ),
        migrations.CreateModel(
            name='MobilityParam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.FloatField()),
                ('mobilitymodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.mobilitymodel')),
            ],
            options={
                'db_table': 'MobilityParam',
            },
        ),
        migrations.CreateModel(
            name='Mobility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempo', models.FloatField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.node')),
            ],
            options={
                'db_table': 'Mobility',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.configuration')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.measure')),
            ],
            options={
                'db_table': 'Measurement',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bw', models.IntegerField(blank=True, null=True)),
                ('delay', models.IntegerField(blank=True, null=True)),
                ('loss', models.IntegerField(blank=True, null=True)),
                ('max_queue_size', models.IntegerField(blank=True, null=True)),
                ('jitter', models.IntegerField(blank=True, null=True)),
                ('int1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='int1', to='configurator.interface')),
                ('int2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='int2', to='configurator.interface')),
            ],
            options={
                'db_table': 'Link',
            },
        ),
        migrations.AddField(
            model_name='interface',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurator.node'),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='configurator.node')),
            ],
            options={
                'db_table': 'Host',
            },
        ),
        migrations.AddField(
            model_name='configuration',
            name='mobilitymodel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configurator.mobilitymodel'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='network',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configurator.network'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='propagationmodel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='configurator.propagationmodel'),
        ),
        migrations.CreateModel(
            name='AccessPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssid', models.CharField(max_length=30)),
                ('mode', models.CharField(max_length=30)),
                ('channel', models.CharField(max_length=30)),
                ('node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='configurator.node')),
            ],
            options={
                'db_table': 'AccessPoint',
            },
        ),
    ]
