# Generated by Django 4.2.3 on 2023-07-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('servicio', models.CharField(max_length=200)),
                ('valor', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]