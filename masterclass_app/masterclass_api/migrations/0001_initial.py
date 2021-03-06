# Generated by Django 2.1 on 2018-08-24 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apprenants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formateurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_hobbies', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='formateurs',
            name='hobbies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterclass_api.Hobbies'),
        ),
        migrations.AddField(
            model_name='apprenants',
            name='formateurs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterclass_api.Formateurs'),
        ),
        migrations.AddField(
            model_name='apprenants',
            name='hobbies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterclass_api.Hobbies'),
        ),
    ]
