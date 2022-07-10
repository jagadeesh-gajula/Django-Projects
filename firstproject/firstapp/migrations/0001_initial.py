# Generated by Django 4.0.4 on 2022-07-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]