# Generated by Django 2.2.1 on 2020-02-13 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsCiudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ModelsEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ModelsEstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadocivil', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ModelsGenero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ModelsOcupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Example3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('apPat', models.CharField(max_length=254)),
                ('apMat', models.CharField(default=False, max_length=254)),
                ('edad', models.BooleanField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelsCiudad')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelsEstado')),
                ('estadocivil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelsEstadoCivil')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelsGenero')),
                ('ocupacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.ModelsOcupacion')),
            ],
            options={
                'db_table': 'Example3',
            },
        ),
    ]
