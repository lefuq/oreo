# Generated by Django 3.1.6 on 2021-02-16 06:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addressee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя адресата')),
                ('photo', models.FilePathField(path='adbk/user_profile_photos', verbose_name='Путь к файлу аватара на сервере')),
                ('sex', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=25, verbose_name='Пол')),
                ('birth', models.DateField(verbose_name='Дата рождения')),
                ('live', models.TextField(max_length=300, verbose_name='Адрес проживания')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_type', models.CharField(choices=[('Городской', 'Городской'), ('Мобильный', 'Мобильный')], max_length=9, verbose_name='Вид телефона (городской/мобильный)')),
                ('phone_number', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(message='Формат номера не соответствует требованиям', regex='[+]\\d{1}\\D\\d{3}\\D\\d{3}\\D\\d{4}')], verbose_name='Номер телефона в формате +7-XXX-XXX-XXXX')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.addressee')),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_type', models.CharField(choices=[('Личная', 'Личная'), ('Рабочая', 'Рабочая')], max_length=7, verbose_name='Вид почты (личная/рабочая)')),
                ('mail_address', models.EmailField(max_length=100, verbose_name='Адрес электронной почты')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.addressee')),
            ],
        ),
    ]
