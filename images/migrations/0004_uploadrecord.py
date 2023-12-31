# Generated by Django 4.2.3 on 2023-07-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_identifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('upload_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
