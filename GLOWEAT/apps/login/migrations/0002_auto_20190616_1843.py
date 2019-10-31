# Generated by Django 2.2.1 on 2019-06-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('edad', models.DateField(default='2000-07-24')),
                ('email', models.EmailField(max_length=254)),
                ('passw', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
