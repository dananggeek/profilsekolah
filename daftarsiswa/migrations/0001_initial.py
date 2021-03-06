# Generated by Django 2.0.4 on 2018-05-19 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pendaftaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depan', models.CharField(max_length=50)),
                ('nama_belakang', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('foto', models.FileField(upload_to='')),
                ('alamat', models.CharField(max_length=100)),
                ('tempat_lahir', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField()),
                ('agama', models.CharField(max_length=50)),
                ('nohp', models.IntegerField()),
                ('nilai_un', models.FileField(upload_to='')),
                ('nama_orangtua', models.CharField(max_length=50)),
                ('alamat_orangtua', models.CharField(max_length=50)),
                ('nohp_orangtua', models.IntegerField()),
                ('tanggal_daftar', models.DateTimeField(auto_now_add=True)),
                ('status_terima', models.BooleanField(default=False)),
            ],
        ),
    ]
