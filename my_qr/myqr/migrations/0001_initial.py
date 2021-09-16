# Generated by Django 3.2.7 on 2021-09-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('dob', models.DateField(blank=True, null=True)),
                ('qr', models.ImageField(null=True, upload_to='my_qr_code')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]