# Generated by Django 4.1.7 on 2023-02-19 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Page_Reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesmodel',
            name='userid',
            field=models.CharField(default='admin', max_length=50),
            preserve_default=False,
        ),
    ]
