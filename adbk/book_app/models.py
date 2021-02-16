from django.db import models
from django.core.validators import RegexValidator


def phone_number_validator():
    return RegexValidator(
        regex=r'[+]\d{1}\D\d{3}\D\d{3}\D\d{4}',
        message='Формат номера не соответствует требованиям')


class Addressee(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя адресата')
    photo = models.FilePathField(
        path="adbk/user_profile_photos",
        verbose_name='Путь к файлу аватара на сервере')
    sex = models.CharField(
        max_length=25,
        verbose_name='Пол',
        choices=[
            ('Мужской', 'Мужской'),
            ('Женский', 'Женский')])
    birth = models.DateField(verbose_name='Дата рождения')
    live = models.TextField(max_length=300, verbose_name='Адрес проживания')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name} (id={self.id})'


class Phone(models.Model):
    user_id = models.ForeignKey('Addressee', on_delete=models.CASCADE)
    phone_type = models.CharField(
        max_length=9,
        choices=[('Городской', 'Городской'), ('Мобильный', 'Мобильный')],
        verbose_name='Вид телефона (городской/мобильный)')
    phone_number = models.CharField(
        max_length=18,
        verbose_name='Номер телефона в формате +7-XXX-XXX-XXXX',
        validators=[phone_number_validator()])


class Mail(models.Model):
    user_id = models.ForeignKey('Addressee', on_delete=models.CASCADE)
    mail_type = models.CharField(
        max_length=7,
        choices=[('Личная', 'Личная'), ('Рабочая', 'Рабочая')],
        verbose_name='Вид почты (личная/рабочая)')
    mail_address = models.EmailField(
        max_length=100,
        verbose_name='Адрес электронной почты')
