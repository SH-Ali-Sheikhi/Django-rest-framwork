# Generated by Django 3.1.4 on 2021-02-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='Images/None/none.jpg', upload_to='Images/'),
        ),
    ]
